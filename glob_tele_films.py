import telebot
import json

films = []


def save():
    with open("films.json", "w", encoding="utf-8") as fm:
        fm.write(json.dumps(films, ensure_ascii=False))
    print("Фильм добавлен в файл films.json")


def load():
    global films
    with open("films.json", "r", encoding="utf-8") as fm:
        films = json.load(fm)


API_TOKEN = "5686028461:AAHuPyaDIuMxgjpdpYhC0O77ksElcj0hnzc"

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["start"])
def start_message(message):
    try:
        load()
        bot.send_message(message.chat.id, "Фильмотека была успешно загружена")
    except:
        films.append("Матрица")
        films.append("Властелин колец")
        films.append("Король говорит")
        films.append("Американский пирог")
        films.append("Над кукушкиным гнездом")
        bot.send_message(
            message.chat.id, "Фильмотека была загружена по умолчанию")


@bot.message_handler(commands=["all"])
def show_all(message):
    bot.send_message(message.chat.id, "Вот список фильмов")
    bot.send_message(message.chat.id, ", ".join(films))


print("Server start")
bot.polling()
