# 📧 AI Email Automation

This project fetches recent Gmail emails, summarizes them using GPT-4o via OpenRouter, and writes the results to a Google Sheet.

## 🔧 Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/ai-email-automation.git
   cd ai-email-automation
2.Install requirements:

bash
Copy
Edit
pip install -r requirements.txt

3.Create a .env file:

ini
Copy
Edit
OPENROUTER_API_KEY=your_api_key_here

4.Place your credentials:

credentials/credentials.json – Gmail OAuth2 credentials

credentials/service_account.json – Google Sheets service account

Run :- 
python main.py

ai-email-automation/
├── credentials/
├── .env
├── main.py
├── email_auth.py
├── gmail_fetcher.py
├── summarizer.py
├── sheets_writer.py
