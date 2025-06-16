# 📧 AI Email Automation

This project reads recent Gmail emails, uses AI (via OpenRouter/GPT-4o) to extract smart summaries, and logs the result into Google Sheets.

## 🔐 Setup
- Put your `credentials.json` and `service_account.json` inside a `credentials/` folder.
- Add `OPENROUTER_API_KEY=your_key_here` to a `.env` file.
- Run: `pip install -r requirements.txt`

## 🚀 Run
```bash
python main.py
