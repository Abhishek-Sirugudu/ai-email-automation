import gspread
import datetime
from google.oauth2.service_account import Credentials

def connect_sheet(service_account_path, spreadsheet_id):
    scopes = ['https://www.googleapis.com/auth/spreadsheets']
    creds = Credentials.from_service_account_file(service_account_path, scopes=scopes)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(spreadsheet_id).sheet1
    sheet.append_row(["Date", "Sender", "Subject", "Summary", "Category", "Urgency", "ActionRequired"])
    return sheet

def insert_summary(sheet, idx, result):
    lines = result.strip().split('\n')
    summary = category = urgency = action = ""
    for line in lines:
        if line.startswith("Summary:"): summary = line.split(":", 1)[1].strip()
        elif line.startswith("Category:"): category = line.split(":", 1)[1].strip()
        elif line.startswith("Urgency:"): urgency = line.split(":", 1)[1].strip()
        elif line.startswith("Action:"): action = line.split(":", 1)[1].strip()

    date_today = datetime.datetime.now().strftime("%Y-%m-%d")
    sender = f"Sender {idx+1}"
    subject = f"Subject {idx+1}"

    sheet.append_row([date_today, sender, subject, summary, category, urgency, action])
    print("✅ Inserted to Google Sheet.")
