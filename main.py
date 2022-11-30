import telebot
from telebot import types

bot = telebot.TeleBot("5944424312:AAF3ttvABVk06IqEi993fpHodRaHyJE95lA")


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
