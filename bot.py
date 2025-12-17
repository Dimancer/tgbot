import os
import telebot

TOKEN = os.environ["BOT_TOKEN"]
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(m):
    bot.reply_to(m, "Привет! Я работаю ✅")

@bot.message_handler(func=lambda m: True)
def echo(m):
    bot.reply_to(m, f"Ты написал: {m.text}")
