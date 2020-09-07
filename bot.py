import telebot
import datetime
import time
import logging

bot = telebot.TeleBot('<-- Acess Token -->')
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard1.row('Расписание', 'Какая сегодня неделя?')


weekday = datetime.datetime.today().weekday()


rasp1 = ['| Расписание на сегодня | 14.50-16.10: лекция смзкт 2/109 |',
         '| Расписание на сегодня | 13.20-16.10: первая подгруппа  тпис 2/310 | вторая подгруппа  гиис 2/411 | 16.20-17.40: лекция гиис  2/209 |',
         '| Расписание на сегодня | 10.00-12.50: первая подгруппа еяиис 3/129 | вторая подгруппа ссп 2/310 | 13.20-14.40: лекция тпис 310 | 14.50-16.10: лекция гиис 2/409 |',
         '| Расписание на сегодня | 14.50-16.10: лекция смзкт 2/109 |',
         '| Расписание на сегодня |\n | 14.50-16.10: лекция еяиис 402 |\n | 16.20-17.40: практика смзкс 2/409 |\n | 17.40 отчёты по практике 2/310 |\n',
         '| ВЫХОДНОЙ МЕН , ОТДЫХАЙ И ЧИЛЬ|', 6, 7, 8]
rasp2 = ['| Чертов понедельник |\n | Расписание на сегодня |\n | 13.20-14.40: лекция ССП каб. 109 |\n | 14.50-16.10: практика ССП каб. 109 |',
         '| Расписание на сегодня | 13.20-16.10: первая подгруппа  тпис 2/310 | вторая подгруппа  гиис 2/411 | 16.20-17.40: лекция гиис  2/209 |',
         '| Расписание на сегодня | 10.00-12.50: первая подгруппа еяиис 3/129 | вторая подгруппа ссп 2/310 | 13.20-14.40: лекция тпис 310 | 14.50-16.10: лекция гиис 2/409 |',
         '| Расписание на сегодня | 14.50-16.10: лекция смзкт 2/109 |',
         '| Расписание на сегодня |\n | 14.50-16.10: лекция еяиис 402 |\n | 16.20-17.40: практика смзкс 2/409 |\n | 17.40 отчёты по практике 2/310 |\n',
         '| ВЫХОДНОЙ МЕН , ОТДЫХАЙ И ЧИЛЬ|', 6, 7, 8]

week1 = '| Верхняя |'
week2 = '| Нижняя |'
click_time = 0


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'расписание':
        print(click_time)
        bot.send_message(
            message.chat.id, rasp2[weekday], reply_markup=keyboard1)
    elif message.text.lower() == 'какая сегодня неделя?':
        bot.send_message(
            message.chat.id, week2)
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as err:
        logging.error(err)
        time.sleep(5)
        print("Internet ERROR!")
