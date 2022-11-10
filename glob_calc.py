import telebot


def calc(exp):
    if exp.find('(') >= 0 and exp.find(')') >= 0:
        # print(exp[:exp.find('(')])
        # print(exp[exp.find(')') + 1:])
        exp = exp[:exp.find(
            '(')] + str(calc(exp[exp.find('(')+1:exp.find(')')])) + exp[exp.find(')') + 1:]
    if exp.find('+') >= 0:
        return calc(exp[:exp.find('+')]) + calc(exp[exp.find('+')+1:])
    if exp.find('-') >= 0:
        return calc(exp[:exp.find('-')]) - calc(exp[exp.find('-')+1:])
    if exp.find('*') >= 0:
        return calc(exp[:exp.find('*')]) * calc(exp[exp.find('*')+1:])
    if exp.find('/') >= 0:
        return calc(exp[:exp.find('/')]) / calc(exp[exp.find('/')+1:])

    return int(exp)


API_TOKEN = "5686028461:AAHuPyaDIuMxgjpdpYhC0O77ksElcj0hnzc"

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["start"])
def show_all(message):
    bot.send_message(message.chat.id, "Бот-калькулятор запущен")


@bot.message_handler(commands=["calc"])
def teke_calc(message):
    qst = message.text[6:]
    qst1 = calc(qst)
    bot.send_message(message.chat.id, f"{qst} = {qst1}")
    # print(qst)


print("Server start")
bot.polling()
