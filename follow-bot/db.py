import firebase_admin
from firebase_admin import credentials, db
import os
from dotenv import load_dotenv

load_dotenv()

cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': os.getenv("FIREBASE_DB_URL")
})

def get_user(user_id):
    ref = db.reference(f'/users/{user_id}')
    return ref.get()

def set_user(user_id, data):
    ref = db.reference(f'/users/{user_id}')
    ref.set(data)

def update_coins(user_id, coins):
    ref = db.reference(f'/users/{user_id}/coins')
    ref.set(coins)

def add_coins(user_id, amount):
    user = get_user(user_id) or {"coins": 0}
    user["coins"] += amount
    set_user(user_id, user)
