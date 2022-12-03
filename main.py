import telebot
from flask import Flask, request
import os

app = Flask(__name__)
TOKEN = os.environ.get('5944424312:AAF3ttvABVk06IqEi993fpHodRaHyJE95lA')
bot = telebot.TeleBot(TOKEN)
# bot = telebot.TeleBot("5944424312:AAF3ttvABVk06IqEi993fpHodRaHyJE95lA")
# should be putted in global variables in OS on Heroku

def main_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    info_Goloseev = telebot.types.KeyboardButton("Інформація про комплекс")
    school_Goloseev = telebot.types.KeyboardButton("Гірськолижна школа")
    rules_Goloseev = telebot.types.KeyboardButton("Правила")
    work_in_alarm = telebot.types.KeyboardButton("Робота під час тривоги")
    reviews = telebot.types.KeyboardButton("Відгуки")

    markup.add(info_Goloseev, rules_Goloseev, school_Goloseev, work_in_alarm, reviews)
    bot.send_message(message.chat.id, f" ", reply_markup=markup)

# Робимо меню
@bot.message_handler(commands=['start'])
def start(message):
    """First main menu of bot"""
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    info_Goloseev = telebot.types.KeyboardButton("Інформація про комплекс")
    school_Goloseev = telebot.types.KeyboardButton("Гірськолижна школа")
    rules_Goloseev = telebot.types.KeyboardButton("Правила")
    work_in_alarm = telebot.types.KeyboardButton("Робота під час тривоги")
    reviews = telebot.types.KeyboardButton("Відгуки")

    markup.add(info_Goloseev, rules_Goloseev, school_Goloseev, work_in_alarm, reviews)
    bot.send_message(message.chat.id, f"Привіт, {message.from_user.first_name} {message.from_user.last_name}!",
                     reply_markup=markup)

@bot.message_handler(content_types=['text'])
def info_goloseev(message):
    if message.text == "Інформація про комплекс":
        """Info menu of bot"""
        pass
    elif message.text.lower().find("школа" or "school" or "навчання") >= 0:
        bot.send_message(message.chat.id, "Ви ввійшли в меню 'Гірськолижна школа'")
        markupSchool = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        info_School = telebot.types.KeyboardButton("Інформація про школу")
        price_School = telebot.types.KeyboardButton("Вартість заняття")
        markupSchool.add(info_School, price_School)
        bot.send_message(message.chat.id, f"Що саме Вас цікавить?", reply_markup=markupSchool)
        bot.register_next_step_handler(message, goloseev_school_function)

    elif message.text.lower().find("правила" or "rules" or "pravila" or "прав") >= 0:
        bot.send_message(message.chat.id, "Ви ввійшли в меню 'Правила'.")
        markupRules = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        school_Rules = telebot.types.KeyboardButton("Правила школи")
        skipass_Rules = telebot.types.KeyboardButton("Правила користування карткою SKI-pass")
        bugil_Rules = telebot.types.KeyboardButton("Правила використування підйомником")
        complex_Rules = telebot.types.KeyboardButton("Правила комплексу")
        markupRules.add(school_Rules, skipass_Rules, bugil_Rules, complex_Rules)
        bot.send_message(message.chat.id, f"Що саме Вас цікавить?", reply_markup=markupRules)
        bot.register_next_step_handler(message, goloseev_rules_function)

    elif message.text.lower().find("тривоги" or "allert" or "безпека") >= 0:
        bot.send_message(message.chat.id, "Ви ввійшли в меню 'Робота під час тривоги'")
        bot.send_message(message.chat.id, "Так же инфа")
        main_menu(message)
    elif message.text.lower().find("відгуки" or "отзыв" or "feedback") >= 0:
        bot.send_message(message.chat.id, "Ви ввійшли в меню 'Відгуки'. Напишіть будь ласка Ваш відгук")
        bot.register_next_step_handler(message, goloseev_reviews_function)
    else:
        bot.send_message(message.chat.id, "Виникла помилка, спробуйте ще раз")
        main_menu(message)

def goloseev_school_function(message):
    if message.text.lower().find("школа" or "school" or "study") >= 0:
        bot.send_message(message.chat.id, "Тут вся инфа или ссылка")
        main_menu(message)

    elif message.text.lower().find("інформація" or "информация" or "information") >= 0:
        bot.send_message(message.chat.id, "Ось всі актуальні ціни:")
        bot.send_message(message.chat.id, "Тут ціни або посилланя або файл")
        main_menu(message)

@bot.message_handler(content_types=['text'])
def info_goloseev_options(message):
    if message.text.lower().find('інфо') >= 0:
        bot.send_message(message.chat.id, f"Загальна інформація про гірку!")
    elif message.text.lower().find('skipass' or 'ski' or 'скай')  >= 0:
        bot.send_message(message.chat.id, f"Ви получаете прайс лист SkiPass и правила")
    elif message.text.lower().find('ціни' or 'цены' or 'price' or 'прайс') >= 0:
        bot.send_document(message.chat.id, 'BQACAgIAAxkBAAEalgJjipEtMIwRF6HG09B05rgtLKE0JQAC8B4AAl2CWEhiYiIEvWrGwCsE' )
    elif message.text.lower().find('контакты' or 'контакти' or 'contacts' or 'телефон') >= 0:
        bot.send_message(message.chat.id, f"Ви в меню Контактной информации")
    elif message.text.lower().find('маршрут' or 'location' or 'map'  or 'адрес') >= 0:
        telebot.types.InlineKeyboardButton(text='Маршрут', url='https://g.page/GoloseevSkiPark')




@bot.message_handler(content_types=['text'])
def general_info(message):


def goloseev_rules_function(message):
    if message.text.lower().find("школа" or "school" or "study") >= 0:
        bot.send_message(message.chat.id, "Тут вся инфа или ссылка")
        main_menu(message)

    elif message.text.lower().find("ski" or "карт" or "pass") >= 0:
        bot.send_message(message.chat.id, "Тут ціни або посилланя або файл")
        main_menu(message)

    elif message.text.lower().find("підйомником" or "бугель" or "lift") >= 0:
        bot.send_message(message.chat.id, "Тут ціни або посилланя або файл")
        main_menu(message)

    elif message.text.lower().find("комплексом" or "goloseev" or "комплекс") >= 0:
        bot.send_message(message.chat.id, "Тут ціни або посилланя або файл")
        main_menu(message)


def goloseev_reviews_function(message):
    pass

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


bot.polling(none_stop=True)