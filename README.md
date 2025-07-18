# 🧠 Mac Grammar Genie

A macOS Shortcut + Python-based workflow that corrects grammar, spelling, and tone in any selected text using OpenAI's GPT model. Built for macOS users who want quick, context-aware editing anywhere (Slack, Gmail, etc.).

---

## ✨ Features

- Fix grammar, spelling, and tone with ChatGPT
- Works anywhere on macOS: Slack, Mail, Threads, Notes, etc.
- Runs via a keyboard shortcut (`⌘ + ⇧ + G`)
- No need to manually open ChatGPT or copy/paste to the browser
- Sends a native macOS notification with the corrected text

---

## 📦 Requirements

- macOS Monterey or later
- Python 3 installed
- [OpenAI API Key](https://platform.openai.com/account/api-keys)
- OpenAI account with billing enabled or free credits

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/mac-grammar-genie.git
cd mac-grammar-genie
```

### 2. Install Python dependencies

```bash
pip3 install -r requirements.txt
```

### 3. Open and configure the macOS Shortcut
*	Open the Mac-Shortcut.shortcut file to import it into the Shortcuts app
*	Edit the shortcut:
*	Find the “Run Shell Script” action
* Replace the placeholders in the script with your details:
  ```bash
  export OPENAI_API_KEY="<YOUR OPENAI API KEY HERE>"
  /<YOUR PYTHON3 LOCATION HERE>/python3 <PATH TO REPOSITORY>/mac-grammar-genie/main.py
  ```
* You can find your Python path by running:
  ```bash
  which python3
  ```

#### 🛡️ Permissions
To allow Shortcuts to simulate copy/paste and send keystrokes:
1.	Go to System Settings → Privacy & Security → Accessibility
2.	Enable:
	•	Shortcuts
	•	Terminal

####  How to Use
1.	Select text anywhere on your Mac (e.g., in Slack, Mail, Notes)
2.	Press ⌘ + ⇧ + G (or the keyboard shortcut you assigned in Shortcuts)
3.	Wait for a few seconds
4.	When you see a notification with the corrected text:
    - Press ⌘ + V to paste the corrected version

Example:
- Input: I thinks this is not going to work but I'm trying anyways
- Output: I think this is not going to work, but I'm trying anyway.

####  Environment Variables Used
*	OPENAI_API_KEY — Your OpenAI secret key
*	OPENAI_MODEL (optional) — Defaults to gpt-3.5-turbo
*	MAC_GRAMMAR_GENIE_PROMPT (optional) — Custom instruction prompt for GPT
