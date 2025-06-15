def is_safe_message(text):
    forbidden_keywords = [
          "زواج", "تعارف", "مساج", "تداول", "استثمار", "جنسية", "ربح مضمون", "فلوس بسرعة",
    "جنس", "اباحي", "اباحية", "صور خاصة", "بنت للتعارف", "زواج مسيار", "مغرية", "إثارة",
    "سكسي", "سكس", "شهوة", "مثير", "محادثات خاصة", "دردشة خاصة", "محتوى خاص", "مطلقة",
    "مضمون 100", "بدون خسارة", "ربح سريع", "تحويل فوري", "عروض مغرية", "مضمون ومجرب",
    "بنات واتساب", "رقم بنت", "فضائح", "فاضح", "صور ساخنة", "بدون قيود", "مغريات",
    "مقاطع خاصة", "فيديو خاص", "مسيار", "ربح أكيد", "دخول سريع", "فلوس فورية"
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
