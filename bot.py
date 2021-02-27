import telebot
bot = telebot.TeleBot('1609593294:AAHbxrlNmME5KHxpGGlfOrpJMkOr5bPMz0c')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)
from telebot import types
math = ["https://4book.org/gdz-reshebniki-ukraina/10-klass/reshebnik-matematika-10-klas-merzlyak-2018-gdz"]
bio = ["https://4book.org/uchebniki-ukraina/10-klass/biologiya-i-ekologiya-10-klas-anderson-2018"]
ist = ["https://4book.org/uchebniki-ukraina/10-klass/vsesvitnya-istoriya-10-klas-ladichenko-2018"]
ph = ["https://4book.org/gdz-reshebniki-ukraina/10-klass/reshebnik-fizika-10-klas-baryahtar-2018-gdz"]
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
     if message.text == "гдз":
          bot.send_message(message.from_user.id, "Привет, держи гдз")
          keyboard = types.InlineKeyboardMarkup()
          key_math = types.InlineKeyboardButton(text='Математика', callback_data='math')
          keyboard.add(key_math)
          key_ist = types.InlineKeyboardButton(text='История', callback_data='ist')
          keyboard.add(key_ist)
          key_bio = types.InlineKeyboardButton(text='Биология', callback_data='bio')
          keyboard.add(key_bio)
          key_ph = types.InlineKeyboardButton(text='Физика', callback_data='ph')
          keyboard.add(key_ph)
          bot.send_message(message.from_user.id, text='Выбери гдз', reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
     if call.data == "math":
          bot.send_message(call.message.chat.id, math)
     elif call.data == "ist":
          bot.send_message(call.message.chat.id, ist)
     elif call.data == "bio":
          bot.send_message(call.message.chat.id, bio)
     elif call.data == "ph":
          bot.send_message(call.message.chat.id, ph)
bot.polling(none_stop=True, interval=0)
