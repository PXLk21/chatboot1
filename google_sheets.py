import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

CREDS_FILE = "credentials.json"
SHEET_ID = os.getenv("SHEET_ID")  # احفظ هذا المتغير في Render

def send_to_sheet(data):
    if not SHEET_ID:
        print("⚠️ لم يتم تحديد SHEET_ID بعد.")
        return

    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_FILE, SCOPES)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(SHEET_ID).worksheet("العروض")

    row = [
        data.get("نوع العقار", ""),
        data.get("المدينة", ""),
        data.get("السعر", ""),
        data.get("جهة التواصل", ""),
        data.get("رابط الإعلان", ""),
    ]
    sheet.append_row(row)
    print("✅ تم الإرسال إلى الشيت بنجاح.")
