import telebot
from telebot import apihelper
import main


proxyDict = {
    "http": "http://117.1.16.131:8080",
    "https": "https://117.1.16.131:8080"
}

def bot_():
    global proxyDict
    dick = main.Dick()
    telebot.apihelper.proxy = proxyDict
    bot = telebot.TeleBot('4522C')

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'Hi! I will make u itmo student...\nSend me your face')

    @bot.message_handler(content_types=["photo"])
    def send_photo(message):

        id_ = message.photo[-1].file_id
        path = bot.get_file(id_)
        print(path)
        download_file = bot.download_file(file_path=path.file_path)

        with open("face.jpg", 'wb') as file:
            file.write(download_file)
        photo = open(dick.penis_on_face("face.jpg"), 'rb')
        bot.send_photo(message.chat.id, photo)
        #request = requests.get(f"https://api.telegram.org/file/bot832044201:AAHjNFU5hV9xSpl7bqbn3CC3yIGDSzyFbHQ/{path}", proxies=proxyDict)
    @bot.message_handler(content_types=['text'])
    def send_text(message):
        pass


    bot.polling(timeout=10**5)


bot_()