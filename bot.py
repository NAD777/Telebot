import telebot

import RPi.GPIO as GPIO  #импорт библиотеки

GPIO.setmode(GPIO.BOARD) #"включение" GPIO

GPIO.setup(7, GPIO.OUT)  #объявление 7-го пина как выход
bot = telebot.TeleBot("407665225:AAG__WuM0socyypxDL74RVZuKFddAtD3JsA")


@bot.message_handler(commands=['help', 'start'])
def comands(message):
    bot.reply_to(message, "/help для отображения команд" + "\n /switch открывает меню" + "\n /uchebnici_7zip или /учебники_7zip - учебники 8 класс архив"+"\n /uchebnici или /учебники - учебники 8 класс")


# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message):
#    if  not(message.text== '/switch'):
#       bot.send_message(message.chat.id, message.text)


@bot.message_handler(commands=['switch'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', 'Убрать меню')
    user_markup.row('/cross', '/учебники_7zip')
    user_markup.row('/led_off ','/led_on')
    user_markup.row('/учебники ')
    user_markup.one_time_keyboard = True
    bot.send_message(message.from_user.id, 'Welcome', reply_markup=user_markup)


@bot.message_handler(commands=['stop'])
def hide_markup(massage):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(massage.from_user.id, 'Hide markup', reply_markup=hide_markup)


@bot.message_handler(commands=['cross'])
def cross(message):
    bot.send_message(message.from_user.id, 'http://pov.sitectors.ru/')
@bot.message_handler(commands=['/led_on'])
def cross(message):
    GPIO.output(7, 1)
    GPIO.cleanup()
@bot.message_handler(commands=['/led_on'])
def cross(message):
    GPIO.output(7, 0)
    GPIO.cleanup()
@bot.message_handler(commands=['uchebnici_7zip','учебники_7zip'])
def uch_7zip(message):
    bot.reply_to(message, "https://drive.google.com/file/d/0B6D0I35T9HrCYlc3eEdQRFVoUWs/view")
@bot.message_handler(commands=['uchebnici','учебники'])
def uch(message):
    bot.reply_to(message, "https://drive.google.com/open?id=0B6D0I35T9HrCajEzcHB3TnhHZjQ")

@bot.message_handler(content_types=["text"])
def root(message):
    print(message.text)
    if( message.text[:4]=='/nad'):
        bot.send_message(message.chat.id, 'Запомненно:'+ message.text[len('/nad'):])
        bot.send_photo(message.chat.id,'https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjevdvQ3JDWAhUDAZoKHdaTCsEQjRwIBw&url=https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdev%3Fid%3D5700313618786177705&psig=AFQjCNE0BfNrw0E6SNz8YDLQ8zI9VZOTRQ&ust=1504792886442980')
bot.polling()
