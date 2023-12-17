import telebot
from telebot import types

bot = telebot.TeleBot('6861435117:AAFmndbTRR8_B0W2Yrg_SQGqU-bbD6MkEsM')


def keyboard(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    iteam1 = types.KeyboardButton('Частые вопросы')
    iteam2 = types.KeyboardButton('Задать вопрос')
    markup.add(iteam1, iteam2)
    bot.send_message(message.chat.id, "Здравствуйте! Я готов ответить на ваши вопросы", reply_markup=markup)

@bot.message_handler(commands= ['start'])
def bot_message(message):
    clava = keyboard(message)

@bot.message_handler(content_types = ['text'])
def bot_message(message):
    if message.chat.type == 'private':

        if message.text == "Частые вопросы":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            iteam1 = types.KeyboardButton('Вопрос 1')
            iteam2 = types.KeyboardButton('Вопрос 2')
            iteam3 = types.KeyboardButton('Вопрос 3')
            iteam4 = types.KeyboardButton('Вопрос 4')
            b = types.KeyboardButton('Назад')
            markup.add(iteam1, iteam2, iteam3, iteam4, b)
            bot.send_message(message.chat.id, "Выбран режим частых вопросов", reply_markup=markup)

        elif message.text == "Назад":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            iteam1 = types.KeyboardButton('Частые вопросы')
            iteam2 = types.KeyboardButton('Задать вопрос')
            markup.add(iteam1, iteam2)
            bot.send_message(message.chat.id, "Назад", reply_markup=markup)

        elif message.text == "Задать вопрос":
            bot.send_message(message.chat.id, "Запишите ваш вопрос")
            
            bot.send_message(message.chat.id, "Ваш запрос отправлен")




bot.polling(none_stop=True)
