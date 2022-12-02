from flask import Flask, request
import telebot
import os

app = Flask(__name__)
TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)
# bot = telebot.TeleBot("5944424312:AAF3ttvABVk06IqEi993fpHodRaHyJE95lA")
# should be putted in global variables in OS on Heroku


# Робимо меню
@bot.message_handler(commands=['start'])
def start(message):
    """First main menu of bot"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    info_Goloseev = types.KeyboardButton("Інформація про комплекс")
    school_Goloseev = types.KeyboardButton("Гірськолижна школа")
    rules_Goloseev = types.KeyboardButton("Правила")
    work_in_alarm = types.KeyboardButton("Робота під час тривоги")
    reviews = types.KeyboardButton("Відгуки")

    markup.add(info_Goloseev, rules_Goloseev, school_Goloseev, work_in_alarm, reviews)
    bot.send_message(message.chat.id, f"Привіт, {message.from_user.first_name} {message.from_user.last_name}!",
                     reply_markup=markup)

@bot.message_handler(content_types=['text'])
def info_goloseev(message):
    if message.text == "Інформація про комплекс":
        """Info menu of bot"""
        markupInfo = types.ReplyKeyboardMarkup(resize_keyboard=True)
        info_gol = types.KeyboardButton("Загальна інформація")
        price_SkiPass = types.KeyboardButton("Вартість SkiPass")
        price_equipment = types.KeyboardButton("Вартість ареди спорядження")
        contacts = types.KeyboardButton("Звя'зок")
        markupInfo.add(info_gol, price_SkiPass, price_equipment, contacts)
        bot.send_message(message.chat.id, f"Радий бачити!", reply_markup=markupInfo)


def info():
    pass
bot.polling(none_stop=True)

@app.route('/' + TOKEN, methods=['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "Python Telegram Bot", 200


@app.route('/')
def main():
    bot.remove_webhook()
    bot.set_webhook(url='https://multipurposechatbot.herokuapp.com/' + TOKEN)
    return "Python Telegram Bot", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))