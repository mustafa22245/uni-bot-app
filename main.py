from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# إنشاء تطبيق FastAPI
app = FastAPI(
    title="تطبيق الحلة الجامعي",
    description="الواجهة الخلفية المحدثة والمستضافة على Vercel",
    version="2.0.0"
)

# إعدادات CORS: ضرورية جداً للسماح لتطبيق الهاتف بالاتصال بالسيرفر
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # يسمح بالاتصال من أي مصدر
    allow_credentials=True,
    allow_methods=["*"],  # يسمح بجميع أنواع العمليات (GET, POST, إلخ)
    allow_headers=["*"],
)

# الصفحة الرئيسية (الرابط الأساسي)
@app.get("/")
async def root():
    return {
        "message": "مرحباً بك في سيرفر تطبيق الحلة الجامعي",
        "status": "online",
        "environment": "Vercel Production"
    }

# رابط لفحص حالة النظام (Health Check)
@app.get("/api/status")
async def get_status():
    return {
        "app": "Hillah University App",
        "version": "2.0.0",
        "server": "Vercel Serverless",
        "connection": "Secure"
    }

# مثال لرابط جلب بيانات (يمكنك توسيعه لاحقاً)
@app.get("/api/info")
async def get_info():
    return {
        "university": "جامعة الحلة",
        "notice": "السيرفر يعمل الآن بنظام التحديث التلقائي من GitHub"
    }
