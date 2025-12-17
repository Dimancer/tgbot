import os
import telebot

TOKEN = os.environ["7777555099:AAH2_mk4YYPQCXNNgjDO2ilkkvxR0syvxmo"]
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(m):
    bot.reply_to(m, "Привет! Я работаю ✅")

@bot.message_handler(func=lambda m: True)
def echo(m):
    bot.reply_to(m, f"Ты написал: {m.text}")
