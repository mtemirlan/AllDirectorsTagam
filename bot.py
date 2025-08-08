import telebot
from telebot import types
from datetime import datetime

TOKEN = "7973079134:AAGvzhLX8Mdkv68VMI6yXgQoPaM1XsRTkeU"
bot = AllDirectorsTagam_bot(TOKEN)

# Команда /start — отправляем кнопку
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Пришёл")
    markup.add(btn)
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

# Обработка нажатия кнопки
@bot.message_handler(func=lambda message: message.text == "Пришёл")
def handle_arrival(message):
    fio = message.from_user.full_name
    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    bot.send_message(message.chat.id, f"✅ Приход зафиксирован\nСотрудник: {fio}\nВремя: {now}")

# На всякий случай обрабатываем любой другой текст
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.send_message(message.chat.id, "Нажмите кнопку 'Пришёл', чтобы отметить приход.")

bot.polling()
