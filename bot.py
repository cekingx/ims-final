import telebot

bot = telebot.TeleBot('872225543:AAE8F2DMZg2XvOhmQvM163zpg1Sw5rV6KKU')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)

@bot.message_handler(func=lambda message: True)
def get_id(message):
    bot.reply_to(message, message.text)
    print(message.chat)
    # bot.send_message(chat_id=372880228, text="halo")


bot.polling()
