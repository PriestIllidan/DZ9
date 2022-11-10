import telebot
import requests



API_URL = "https://7012.deeppavlov.ai/model"
API_TOKEN = "5686028461:AAHuPyaDIuMxgjpdpYhC0O77ksElcj0hnzc"

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=["start"])
def show_all(message):
    bot.send_message(message.chat.id, "Бот поиска по запросу начал работу!")

@bot.message_handler(commands=["wiki"])
def wiki(message):
    qst = message.text.split()[1:]
    qst_str = " ".join(qst)
    data = {"question_raw": [qst_str]}
    try:
        res = requests.post(API_URL, json=data, verify=False).json()
        bot.send_message(message.chat.id, res)
    except:
        bot.send_message(message.chat.id, "Ничего не найдено")



print("Server start")
bot.polling()