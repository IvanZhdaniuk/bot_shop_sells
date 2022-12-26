# pip install pytelegrambotapi


import telebot
from telebot import types

bot = telebot.TeleBot('5730541647:AAE5TzJfqUeXuPQ6XGm7L5f7cy_nuZYHdwQ');




# @bot.message_handler(commands=['Start', 'Help'])
# def send_welcome(message):
#     bot.reply_to(message, "Привет, приветсвую тебя в самом продвинутом телеграм канале, здесь ты как в конструкторе"
#                           " можешь собрать все интересующие тебя уведомленияю: новости, курсы валют, и даже обновления"
#                           " твоих рузей в Instogtram.")

# @bot.message_handler(commands=['Start', 'Help']
# def send_welcome(message):
#     markup = types.ReplyKeyboardMarkup(row_width=2)
#     itembtn1 = types.KeyboardButton('a')
#     itembtn2 = types.KeyboardButton('v')
#     itembtn3 = types.KeyboardButton('d')
#     markup.add(itembtn1, itembtn2, itembtn3)
#     bot.send_message(chat_id, "Choose one letter:", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def echo_all(message):


        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('Подписаться на гороскоп')
        # itembtn2 = types.KeyboardButton('v')
        # itembtn3 = types.KeyboardButton('d')
        markup.row(itembtn1)
        bot.send_message(message.from_user.id, "Choose one letter:", reply_markup=markup)






# def get_text_messages(message):
# # @bot.message_handler(content_types=['text', 'document', 'audio']) '''mabi that too'''
#
#     if message.text == "Привет":
#         bot.send_message(message.from_user.id, "Привет чем могу помочь?")
#     elif message.text =="/help":
#         bot.send_message(message.from_user.id, "Напиши привет")
#     else:
#         bot.send_message(message.from_user.id, "Я тебя не помню напиши '/help'")


"""Проверка новых сообщений"""
bot.polling(none_stop=True, interval=0)

