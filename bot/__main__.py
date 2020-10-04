from bot.table import get_schedule_by_date

import telebot

import os
import time
import json
import logging

credentials_path = os.path.join('bot', 'credentials.json')
with open(credentials_path) as file:
    token = json.load(file)['token']

bot = telebot.TeleBot(token)
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.row('Расписание', 'Завтра')


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Initialized', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message: telebot.types.Message):
    chat_id = message.chat.id
    if message.text.lower() == 'расписание':
        schedule = get_schedule_by_date('today')
        bot.send_message(chat_id, schedule, reply_markup=keyboard)
    elif message.text.lower() == 'завтра':
        schedule = get_schedule_by_date('tomorrow')
        bot.send_message(chat_id, schedule, reply_markup=keyboard)
    else:
        bot.send_message(chat_id, 'Unknown command', reply_markup=keyboard)


def main():
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as err:
            logging.error(err)
            time.sleep(5)
            print('Internet ERROR!')


if __name__ == '__main__':
    main()
