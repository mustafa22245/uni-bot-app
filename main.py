from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# تعريف التطبيق واسمه
app = FastAPI(title="تطبيق الحلة الجامعي - الخادم")

# إعداد CORS للسماح لتطبيق الواجهة (الهاتف أو الويب) بالاتصال بالسيرفر
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # يسمح بالاتصال من أي تطبيق. (يمكنك لاحقاً تحديد رابط تطبيقك فقط)
    allow_credentials=True,
    allow_methods=["*"],  # يسمح بجميع أنواع الطلبات (GET, POST, PUT, DELETE)
    allow_headers=["*"],
)

# الصفحة الرئيسية للسيرفر
@app.get("/")
def read_root():
    return {
        "status": "success",
        "message": "أهلاً بك! سيرفر تطبيق الحلة الجامعي يعمل بنجاح."
    }

# رابط إضافي لاختبار حالة السيرفر (مفيد لتطبيق الهاتف للتحقق من الاتصال)
@app.get("/api/health")
def health_check():
    return {
        "status": "active",
        "platform": "Vercel",
        "app_name": "Hillah Uni App"
    }
