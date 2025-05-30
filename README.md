# 🚀 AnonLFI - Local File Inclusion (LFI) Automation Tool

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)

> A sleek, terminal-based toolkit to hunt and exploit Local File Inclusion (LFI) vulnerabilities — fast, modular, and built for real-world recon.

---

## 📌 Features

🎯 Fast Detection of Local File Inclusion (LFI) Vulnerabilities
Quickly identifies LFI issues in web applications using efficient scanning techniques.

🔍 Dynamic Payload Selection
Offers the flexibility to either use a built-in default payload wordlist or supply your own custom wordlist during runtime.

⚙️ Thread Handling Support
Boost scan performance by configuring the number of concurrent threads—default is 50, but easily customizable by the user.

🧠 Intelligent Prompting System
Automatically prompts users to specify a custom wordlist and thread count when selecting the AnonLFI module, enhancing user control without adding complexity.

📊 Real-Time Detection Feedback
Provides immediate visual feedback through the terminal, including detection status and options to exploit or interact further upon successful identification.

🧠 Modular Architecture
Designed for extensibility, allowing easy integration of new modules or vulnerability checkers in the future.

🎨 Interactive Terminal UI
Built using rich and prompt_toolkit for a visually appealing, interactive, and user-friendly command-line experience.

🤖 Made for Hackers by Hackers
Purpose-built for penetration testers, CTF players, and bug bounty hunters to simplify and automate LFI discovery and exploitation.


---

## 📷 Preview

```bash
_______                        ______ __________________
___    |_______ ______ _______ ___  / ___  ____/____  _/
__  /| |__  __ \_  __ \__  __ \__  /  __  /_     __  /  
_  ___ |_  / / // /_/ /_  / / /_  /____  __/    __/ /   
/_/  |_|/_/ /_/ \____/ /_/ /_/ /_____//_/       /___/   

       Tool: AnonLFI   Author: ANONDGR (Rajan Kumar Barik)

>>> Enter Target URL For Testing: http://example.com/index.php?page=home

>>> Select Options:
1: AnonLFI
2: Change Target
3: Quit
```

---

## ⚙️ Installation

```bash
git clone https://github.com/DIGITALRAJAN22M/AnonLFI.git
cd AnonLFI
pip install -r requirements.txt
```

> ⚠️ Ensure you're using Python **3.8+**

---

## 🕹️ Usage

```bash
python AnonLFI.py or python3 AnonLFI.py
```

Then follow the interactive prompts to:

- Enter a target URL
- Scan for LFI vulnerabilities
- Exploit detected vulnerabilities (e.g., view `/etc/passwd`)
- Change the target or exit cleanly

---

## 📁 Project Structure

```
LFIHunt/
├── AnonLFI.py             # Main CLI launcher and interface
├── README.md              # Project documentation
├── requirements.txt       # Required Python dependencies
├── payloads/              # Payload files for LFI fuzzing
│   ├── large_payloads.txt
│   └── small_payloads.txt
├── vault/                 # Core logic of AnonLFI
│   ├── AnonLFI.py   
```

---

## 📚 Dependencies

- `rich`
- `prompt_toolkit`

Install them via:

```bash
pip install -r requirements.txt
```

---

## ⚠️ Disclaimer

This tool is for **authorized testing and educational purposes only**.

> Using AnonLFI on systems without **explicit, legal authorization** is illegal and unethical.

- You are solely responsible for any misuse or damage.
- The creator **assume no liability**.
- Always stay in scope, follow laws, and respect terms of engagement.

**Hack smart. Hack legal. Hack with purpose.**

---

## 👨‍💻 Author

**🔐 Rajan Kumar Barik (aka ANONDGR)**  
> *Built with ❤️ for the cybersecurity community.*

---
## 🎬 Demo Video  
🎥 **Watch the tool in action here**:  
[![AnonLFI Demo](https://img.youtube.com/vi/oQpljfH4okY/0.jpg)](https://www.youtube.com/watch?v=oQpljfH4okY)



🔗 Connect with the Author
Want to collaborate, learn together, or just vibe on cybersecurity?
Find me across the digital realm:

🌐 Portfolio: https://digitalrajan22m.github.io/anondgr [anondgr]

💻 GitHub: @DIGITALRAJAN22M [DIGITALRAJAN22M]

🔗 LinkedIn: https://www.linkedin.com/in/rajan-kumar-barik-719954276/ [Rajan Kumar Barik]

✍️ Medium Blog: https://medium.com/@rajankumarbarik143 [rajankumarbarik143]

🐦 Twitter/X: https://x.com/Rajan22m [Rajan22m]

🎮 Discord: https://discord.gg/vpU8xzSQ [ANONDGR]

📺 YouTube: https://www.youtube.com/@digitalrajan22m?sub_confirmation=1  [DIGITALRAJAN22M]

☕ Built with curiosity, chaos, and code — stay connected!


