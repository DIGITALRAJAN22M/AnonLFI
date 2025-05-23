from rich.console import Console
from prompt_toolkit import HTML, PromptSession
from prompt_toolkit.history import InMemoryHistory

from vault.AnonLFI import AnonLFI

console = Console()

class Module:
    def __init__(self, url, checker_class, check_method, action):
        self.url = url
        self.checker_class = checker_class
        self.check_method = check_method
        self.action = action
        self.checker = self.checker_class(self.url, silent=False)

    def update_url(self, new_url):
        self.url = new_url
        self.checker = self.checker_class(self.url, silent=False)

    def run(self):
        # For AnonLFI module, prompt for custom payload wordlist and threads
        if self.checker_class is AnonLFI:
            # Wordlist prompt
            use_custom = console.input("[bold blue]Do You Want To Use custom payload Wordlist? ([green]Y[/green]/[red]n[/red]): ")
            if use_custom.strip().lower() in ('y', 'yes'):
                path = console.input("[bold blue]Enter Full Path to Wordlist: ")
                try:
                    self.checker.wordlist = path
                except Exception:
                    console.print(f"[bold red]Failed to set custom wordlist path: {path}[/bold red]")
            # Threads prompt
            thread_input = console.input("[bold blue]Specify number of threads ([green]default 50[/green]): ")
            if thread_input.strip().isdigit():
                try:
                    self.checker.threads = int(thread_input.strip())
                except Exception:
                    console.print(f"[bold red]Failed to set threads count: {thread_input}[/bold red]")

        # Run the vulnerability check
        result, param_name = getattr(self.checker, self.check_method)()
        if result:
            console.print(f"[bold white]Oh No !! LFI detected ([magenta]{self.checker.__class__.__name__}[/magenta]):[/bold white] {result}")
        else:
            console.print(f"[bold green]🟢 Scan complete: No LFI issues discovered. ({self.checker.__class__.__name__}).[/bold green]")

        # Handle exploitation actions if any
        if result == True and self.action:
            choice = console.input(f"[bold blue]Select an action (1: [green]{self.action}[/green], 2: [red]Skip[/red]): ")
            if choice == "1":
                if self.action == "Run shell":
                    getattr(self.checker, self.action.lower().replace(" ", "_"))(param_name)
                elif self.action == "Exploit file":
                    filename = console.input('Enter filename to display: ')
                    getattr(self.checker, self.action.lower().replace(" ", "_"))(filename, param_name)


def banner():
    banner = '''[bold blue]
_______                        ______ __________________
___    |_______ ______ _______ ___  / ___  ____/____  _/
__  /| |__  __ \\_  __ \\__  __ \\__  /  __  /_     __  /  
_  ___ |_  / / // /_/ /_  / / /_  /____  __/    __/ /   
/_/  |_|/_/ /_/ \\____/ /_/ /_/ /_____//_/       /___/   

       [cyan]Tool:[/cyan][green] AnonLFI[/green]   [cyan]Author:[/cyan][green] ANONDGR (Rajan Kumar Barik)[/green]
'''
    console.print(banner, style="bold magenta")


def main():
    banner()

    url_session = PromptSession(history=InMemoryHistory())
    cmd_session = PromptSession(history=InMemoryHistory())

    url = url_session.prompt(HTML('<b><ansiblue>Enter Target URL For Testing: </ansiblue></b>'))

    modules = [
        Module(url, AnonLFI, "path_traversal_checker", None)
    ]

    while True:
        try:
            console.print("\n[bold blue]Select Options:[/bold blue]")
            for i, module in enumerate(modules, 1):
                console.print(f"[bold cyan]{i}[/bold cyan]: [bold green]{module.checker.__class__.__name__}[/bold green]")

            console.print(f"[bold cyan]{len(modules) + 1}[/bold cyan]: [bold green]Change Target[/bold green]")
            console.print(f"[bold cyan]{len(modules) + 2}[/bold cyan]: [bold red]Quit[/bold red]")

            while True:
                choice = cmd_session.prompt(HTML('<b><ansired>></ansired><ansiblue>></ansiblue><ansigreen>></ansigreen></b> '))
                if choice.isdigit():
                    idx = int(choice)
                    if 1 <= idx <= len(modules):
                        modules[idx - 1].run()
                        break
                    elif idx == len(modules) + 1:
                        url = url_session.prompt(HTML('<b><ansiblue>Enter new Target URL to test: </ansiblue></b>'))
                        for module in modules:
                            module.update_url(url)
                        break
                    elif idx == len(modules) + 2:
                        console.print("[bold green]Goodbye ANONDGR! Stay safe out there.[/bold green]")
                        return
                    else:
                        console.print("[bold red]Oh No ! Invalid Option You Have Choosed Try Again ! [/bold red]")
                elif choice == "":
                    continue
                else:
                    console.print("[bold red]Oh No ! Invalid Option You Have Choosed Try Again ![/bold red]")

        except KeyboardInterrupt:
            console.print("\n[bold blue]See You Again ANONDGR ![/bold blue]") 
            break

if __name__ == '__main__':
    main()
