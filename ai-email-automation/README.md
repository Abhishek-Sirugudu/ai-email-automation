Here is your full `README.md` file content, ready to copy-paste directly or save as a file:

---

### 📄 `README.md`

````markdown
# 📧 AI Email Automation

This project reads recent Gmail emails, summarizes them using AI (via OpenRouter), and logs the results into a Google Sheet.

---

## 🔧 Setup

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
````

2. **Create a `.env` file**

   Inside your project root:

   ```
   OPENROUTER_API_KEY=your_api_key_here
   ```

3. **Add credentials**

   Place your credential files as follows:

   ```
   credentials/
   ├── credentials.json          # Gmail OAuth2 credentials
   └── service_account.json      # Google Sheets service account
   ```

4. **Make sure `.gitignore` includes:**

   ```
   .env
   credentials/
   ```

---

## 🚀 Run

To start the automation:

```bash
python main.py
```

---

## 📁 Project Structure

```
ai-email-automation/
├── credentials/                # Private credentials folder
│   ├── credentials.json
│   └── service_account.json
├── .env                        # API key for OpenRouter
├── .gitignore
├── README.md
├── requirements.txt
├── main.py                     # Main runner script
├── email_auth.py               # Gmail OAuth2 handler
├── gmail_fetcher.py            # Fetch unread emails
├── summarizer.py               # AI summarization logic
├── sheets_writer.py            # Write summaries to Google Sheets
```

---

## 📬 Output

* Emails are fetched from your Gmail inbox.
* Summaries are generated using GPT-4o via OpenRouter.
* Summaries are logged into a Google Sheet using your service account.

---

## 🛡️ Warning

Never upload `.env` or files in `credentials/` to GitHub. These contain sensitive keys.

---

```

Let me know if you want a markdown badge version or advanced formatting.
```
