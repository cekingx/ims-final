from flask import Flask, request
import requests
import telebot

bot = telebot.TeleBot('872225543:AAE8F2DMZg2XvOhmQvM163zpg1Sw5rV6KKU')
app = Flask(__name__)
url = "http://localhost:5001/inbox"


@app.route("/")
def hello():
    return "This is gate"


@app.route('/send', methods=['POST'])
def send():
    req_data = request.get_json()
    chat_id = req_data['chat_id']
    nama = req_data['nama']
    msg = f'Hallo {nama}'
    bot.send_message(chat_id=chat_id, text=msg)
    return msg


# @bot.message_handler(func=lambda message: True)
# def reply(message):
#     chat_id = message.chat.id
#     nama = message.chat.first_name
#     data = {"chat_id": chat_id, "nama": nama}
#     requests.post(url, json=data)
#     bot.reply_to(message, "Pesan anda sedang diproses")


# bot.polling()
