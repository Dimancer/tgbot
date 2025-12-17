import os
from flask import Flask, request, abort
import telebot
from bot import bot

SECRET = os.environ["WEBHOOK_SECRET"]

app = Flask(__name__)

@app.get("/")
def index():
    return "OK", 200

@app.post(f"/webhook/{SECRET}")
def webhook():
    if request.headers.get("content-type") != "application/json":
        abort(403)

    update = telebot.types.Update.de_json(request.get_data().decode("utf-8"))
    bot.process_new_updates([update])
    return "OK", 200
