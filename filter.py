def is_safe_message(text):
    forbidden_keywords = [
        "زواج", "تداول", "استثمار", "جنسية", "ربح مضمون", "اباحي", "اباحية", "جنس"
    ]
    return not any(word in text.lower() for word in forbidden_keywords)

def extract_info(text):
    lines = text.strip().splitlines()
    data = {"نوع العقار": "", "المدينة": "", "السعر": "", "جهة التواصل": "", "رابط الإعلان": ""}

    for line in lines:
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if key in data:
                data[key] = value
            elif key == "رابط الموقع":
                data["رابط الإعلان"] = value

    if all(data.values()):
        return data
    return None
