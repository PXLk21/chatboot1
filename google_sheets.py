import gspread
from oauth2client.service_account import ServiceAccountCredentials

SPREADSHEET_NAME = "RealEstateAds"
SCOPES = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDS_FILE = "credentials.json"

def send_to_sheet(data):
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_FILE, SCOPES)
    client = gspread.authorize(creds)
    sheet = client.open_by_key("1Pig1Kvp47szTIkdhh1vE82YjfjPE0isA").sheet1

    row = [
        data["نوع العقار"],
        data["المدينة"],
        data["السعر"],
        data["جهة التواصل"],
        data["رابط الإعلان"],
    ]
    sheet.append_row(row)
