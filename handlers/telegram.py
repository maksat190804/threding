import telebot

def send_notify(message):
    bot = telebot.TeleBot("41186852ed689efe1866cd5db7aad226")
    bot.send_message(1077806658, message)