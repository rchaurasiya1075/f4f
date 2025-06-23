import telebot
import os
from dotenv import load_dotenv
from db import get_user, add_coins

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    uid = msg.from_user.id
    user = get_user(uid)
    if not user:
        add_coins(uid, 0)
    bot.reply_to(msg, "👋 Welcome to FollowX Bot!\nUse /earn to start earning coins.")

@bot.message_handler(commands=['balance'])
def balance(msg):
    uid = msg.from_user.id
    user = get_user(uid) or {"coins": 0}
    bot.reply_to(msg, f"💰 Your balance: {user['coins']} coins")

@bot.message_handler(commands=['earn'])
def earn(msg):
    # Replace with actual links
    links = [
        "https://youtube.com/example1",
        "https://instagram.com/example2",
        "https://t.me/example3"
    ]
    reply = "🔗 Follow these and reply 'Done' to earn coins:\n\n"
    for l in links:
        reply += f"👉 {l}\n"
    bot.send_message(msg.chat.id, reply)

@bot.message_handler(func=lambda m: m.text.lower() == "done")
def task_done(msg):
    add_coins(msg.from_user.id, 5)
    bot.reply_to(msg, "✅ Coins added! Use /balance to check.")

bot.infinity_polling()
