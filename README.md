# 🤖 AI Windows Assistant

A simple offline AI-based assistant that helps users troubleshoot basic system-related issues and execute quick fixes securely via PIN confirmation.

Built with Python and Streamlit, this assistant matches user questions to predefined intents and safely executes local commands.

---

## 🔍 Features

- Detects common user issues like "Internet not working", "Start Menu frozen", etc.
- Matches issues to pre-defined intents via `intents.json`
- Executes safe system actions (like network resets) using Python/Bash
- PIN-protected command execution for added security
- Action logs with timestamp and command status
- Fully offline – no OpenAI API or external APIs used

---

## 🚀 Try It Live

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-windows-assistant.streamlit.app)

> Hosted on [Streamlit Cloud](https://streamlit.io/cloud)

---

## 🧰 Tech Stack

| Tech        | Purpose                    |
|-------------|----------------------------|
| Python      | Core logic and backend     |
| Streamlit   | Web interface              |
| JSON        | Intent routing file        |
| Bash/Python | Command execution          |
| GitHub      | Version control            |

---

## ⚙️ How to Run Locally

```bash
git clone https://github.com/DevAhmadz/AI-Windows-Assistant.git
cd AI-Windows-Assistant
pip install -r requirements.txt
streamlit run app.py
