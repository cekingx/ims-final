from flask import Flask, request
import telebot

bot = telebot.TeleBot('872225543:AAE8F2DMZg2XvOhmQvM163zpg1Sw5rV6KKU')
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/send", methods=['POST'])
def send():
    req_data = request.get_json()
    msg = req_data['msg']
    bot.send_message(chat_id=372880228, text=msg)
    return msg
