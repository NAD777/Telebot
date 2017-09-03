
import telebot

bot = telebot.TeleBot("407665225:AAG__WuM0socyypxDL74RVZuKFddAtD3JsA")

@bot.message_handler(commands=['help','start'])
def comands(message):
	bot.reply_to(message, "/help для отображения команд"+"\n /switch открывает меню ")


#@bot.message_handler(content_types=["text"])
#def repeat_all_messages(message):
#    if  not(message.text== '/switch'):
 #       bot.send_message(message.chat.id, message.text)


@bot.message_handler(commands = ['switch'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True,False)
    user_markup.row('/start','Убрать меню')
    user_markup.row('/cross','2','3')
    user_markup.row('1', '2', '3')
    user_markup.row('1', '2', '3')
    user_markup.one_time_keyboard = True
    bot.send_message(message.from_user.id,'Welcome',reply_markup=user_markup)
@bot.message_handler(commands = ['stop'])
def hide_markup(massage):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(massage.from_user.id, 'Hide markup', reply_markup=hide_markup)
@bot.message_handler(commands=['cross'])
def comands(message):
    bot.send_message(message.from_user.id, 'http://pov.sitectors.ru/')
bot.polling()