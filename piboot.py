import telebot

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
bot = telebot.TeleBot("407665225:AAG__WuM0socyypxDL74RVZuKFddAtD3JsA")
@bot.message_handler(commands=['switch'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/led_off ','/led_on')

    user_markup.one_time_keyboard = True
    bot.send_message(message.from_user.id, 'Welcome', reply_markup=user_markup)


@bot.message_handler(commands=['/led_on'])
def cross(message):
    GPIO.output(7, 1)
    GPIO.cleanup()
@bot.message_handler(commands=['/led_off'])
def cross(message):
    GPIO.output(7, 0)
    GPIO.cleanup()

bot.polling()
