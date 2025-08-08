import telebot
from telebot import types
from datetime import datetime

TOKEN = "7973079134:AAGvzhLX8Mdkv68VMI6yXgQoPaM1XsRTkeU"
bot = telebot.TeleBot(TOKEN)

# Команда /start — отправляем кнопки
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Пришёл")
    btn2 = types.KeyboardButton("Ушёл")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

# Обработка нажатия "Пришёл"
@bot.message_handler(func=lambda message: message.text == "Пришёл")
def handle_arrival(message):
    fio = f"{message.from_user.first_name} {message.from_user.last_name or ''}".strip()
    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    bot.send_message(message.chat.id, f"✅ Приход зафиксирован\nСотрудник: {fio}\nВремя: {now}")

# Обработка нажатия "Ушёл"
@bot.message_handler(func=lambda message: message.text == "Ушёл")
def handle_departure(message):
    fio = f"{message.from_user.first_name} {message.from_user.last_name or ''}".strip()
    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    bot.send_message(message.chat.id, f"🚪 Уход зафиксирован\nСотрудник: {fio}\nВремя: {now}")

# Любой другой текст
@bot.message_handler(func=lambda message: True)
def default_response(message):
    bot.send_message(message.chat.id, "Пожалуйста, нажмите кнопку 'Пришёл' или 'Ушёл'.")

bot.polling()



