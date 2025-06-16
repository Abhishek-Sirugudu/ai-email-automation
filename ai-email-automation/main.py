# main.py

from email_auth import authenticate_gmail
from gmail_fetcher import fetch_emails
from summarizer import summarize_emails
from sheets_writer import write_to_sheets

def main():
    print("🔐 Authenticating Gmail...")
    service = authenticate_gmail()

    print("📥 Fetching emails...")
    emails = fetch_emails(service)

    if not emails:
        print("⚠️ No new emails found.")
        return

    print(f"✉️ {len(emails)} emails fetched. Summarizing...")
    summaries = summarize_emails(emails)

    print("📊 Writing summaries to Google Sheets...")
    write_to_sheets(summaries)

    print("✅ Done! All emails processed and logged.")

if __name__ == "__main__":
    main()
