from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
import json
import os
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_FILE = "bot_data.json"

def load_db():
    if not os.path.exists(DATA_FILE):
        return {"categories": {}, "tips": ["مرحباً بك في تطبيق الحلة الجامعي"]}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_db(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

@app.get("/")
def home():
    return {"status": "online", "message": "Server is running perfectly!"}

@app.get("/get_db")
async def get_db():
    return load_db()

@app.post("/save_db")
async def save_all(data: dict = Body(...)):
    save_db(data)
    return {"status": "success"}

@app.get("/get_tip")
async def get_tip():
    db = load_db()
    return {"tip": random.choice(db.get("tips", ["بالتوفيق في دراستك"]))}

@app.get("/get_categories")
async def get_categories():
    return list(load_db().get("categories", {}).keys())

@app.get("/get_files/{cat}")
async def get_files(cat: str):
    return load_db().get("categories", {}).get(cat, {})

