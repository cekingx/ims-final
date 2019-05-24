import telegram
import requests
import json
bot = telegram.Bot('872225543:AAE8F2DMZg2XvOhmQvM163zpg1Sw5rV6KKU')


def gate(request):
    data = request.get_json(force=True)
    update = telegram.Update.de_json(data, bot)
    INBOX_ENDPOINT = "https://us-central1-proud-woods-237806.cloudfunctions.net/inbox"

    raw_data = {
        "chat_id": 372880228,
        "in_msg": "lorem ipsum",
        "flag": "0"
    }

    # Ketika request datang dari engine outbox
    if "from_outbox" in data:
        chat_id = data['chat']['id']
        tipe = data['chat']['tipe']
        bot.sendMessage(chat_id=chat_id,
                        text=f"Pesan yang anda kirim bertipe {tipe}")

    # Ketika request datang dari bot
    # TODO: Handler pesan bertipe msg
    elif "text" in data['message']:
        raw_data['chat_id'] = data['message']['chat']['id']
        raw_data['in_msg'] = data['message']['text']
        raw_data['flag'] = "1"
        json_data = json.dumps(raw_data)
        requests.post(url=INBOX_ENDPOINT, data=json_data)

    # TODO: Handler pesan bertipe file
    elif "document" in data['message']:
        raw_data['chat_id'] = data['message']['chat']['id']
        raw_data['in_msg'] = data['message']['document']['file_name']
        raw_data['flag'] = "2"
        json_data = json.dumps(raw_data)
        requests.post(url=INBOX_ENDPOINT, data=json_data)

    # TODO: Handler pesan bertipe loc
    elif "location" in data['message']:
        raw_data['chat_id'] = data['message']['chat']['id']
        raw_data['in_msg'] = "Lokasi"
        raw_data['flag'] = "3"
        json_data = json.dumps(raw_data)
        requests.post(url=INBOX_ENDPOINT, data=json_data)

    # TODO: Handler pesan bertipe img
    elif "photo" in data['message']:
        raw_data['chat_id'] = data['message']['chat']['id']
        raw_data['in_msg'] = "Foto"
        raw_data['flag'] = "4"
        json_data = json.dumps(raw_data)
        requests.post(url=INBOX_ENDPOINT, data=json_data)

    else:
        chat_id = update.message.chat.id
        bot.sendMessage(chat_id=chat_id, text="Tipe pesan tidak dikenali")
