from google_sheets import send_to_sheet

data = {
    "نوع العقار": "شقة",
    "المدينة": "الرياض",
    "السعر": "500000",
    "جهة التواصل": "واتساب",
    "رابط الإعلان": "https://example.com"
}

send_to_sheet(data)
