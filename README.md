# Real Estate Telegram Bot

## ✅ الوظيفة:
بوت تيليجرام يستقبل إعلانات عقارية من الرسائل وينسخها مباشرة إلى Google Sheets، مع تصفية المحتوى غير المرغوب فيه.

## 📦 الملفات:
- `bot.py`: كود البوت الرئيسي
- `filter.py`: يحتوي على كلمات ممنوعة وطريقة استخراج البيانات
- `google_sheets.py`: إرسال البيانات إلى Google Sheets
- `requirements.txt`: مكتبات التشغيل
- `credentials.json`: مفتاح Google API (ترفعه يدويًا)
- `Procfile`: إن احتجته لـ Render

## 🔧 المتطلبات:
1. أنشئ Google Sheet جديد باسم `RealEstateAds`، وضع فيه الأعمدة التالية:
    - نوع العقار | المدينة | السعر | جهة التواصل | رابط الإعلان

2. من Google Cloud Platform:
    - أنشئ credentials بصيغة `Service Account Key (JSON)`
    - حمّل الملف وسمّه `credentials.json`

3. على Render:
    - اربط مستودع GitHub يحوي هذه الملفات
    - أنشئ Web Service
    - اضبط متغير بيئة `BOT_TOKEN`

## ✅ جاهز للتعديل أو التشغيل المباشر
- الكود منظم وواضح ويمكنك التعديل على كلمات الحظر أو طريقة التحليل بسهولة.

