# pip install telebot==0.0.5
from telebot import *
from dataclasses import *
import os

@dataclass
class User:
    name: str
    tg_id: int
    test1: int
    test2: int
    test3: int
    test4: int
    test5: int

users = {}

bot = TeleBot("", skip_pending=True)

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, "Добро пожаловать! Введите имя", reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(m, get_name1)

@bot.message_handler(content_types=["text"])
def get_name1(message):
    user_id = message.from_user.id
    user_name = message.text
    user = User(name=user_name, tg_id=user_id, test1=0, test2=0, test3=0, test4=0, test5=0)
    users[user_id] = user
    show_test1(message)

@bot.message_handler(content_types=["text"])
def show_test1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton("ОТВЕТ")
    btn2 = types.KeyboardButton("Ответ 2")
    btn3 = types.KeyboardButton("Ответ 3")
    btn4 = types.KeyboardButton("Ответ 4")
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    bot.send_message(message.chat.id, "Вопрос #1. <вопрос1>", reply_markup=markup)
    bot.register_next_step_handler(message, check_test1)

@bot.message_handler(content_types=["text"])
def check_test1(message):
    user_id = message.from_user.id
    user_answer = message.text
    user = users[user_id]
    correct_answer = "ОТВЕТ"
    if user_answer == correct_answer:
        user.test1 = 1
        users[user_id] = user
    print(user)
    show_test2(message)


@bot.message_handler(content_types=["text"])
def show_test2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton("ОТВЕТ")
    btn2 = types.KeyboardButton("Ответ 2")
    btn3 = types.KeyboardButton("Ответ 3")
    btn4 = types.KeyboardButton("Ответ 4")
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    bot.send_message(message.chat.id, "Вопрос #2. <вопрос2>", reply_markup=markup)
    bot.register_next_step_handler(message, check_test2)

@bot.message_handler(content_types=["text"])
def check_test2(message):
    user_id = message.from_user.id
    user_answer = message.text
    user = users[user_id]
    correct_answer = "ОТВЕТ"
    if user_answer == correct_answer:
        user.test2 = 1
        users[user_id] = user
    print(user)
    show_test3(message)


@bot.message_handler(content_types=["text"])
def show_test3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton("ОТВЕТ")
    btn2 = types.KeyboardButton("Ответ 2")
    btn3 = types.KeyboardButton("Ответ 3")
    btn4 = types.KeyboardButton("Ответ 4")
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    bot.send_message(message.chat.id, "Вопрос #3. <вопрос3>", reply_markup=markup)
    bot.register_next_step_handler(message, check_test3)


@bot.message_handler(content_types=["text"])
def check_test3(message):
    user_id = message.from_user.id
    user_answer = message.text
    user = users[user_id]
    correct_answer = "ОТВЕТ"
    if user_answer == correct_answer:
        user.test3 = 1
        users[user_id] = user
    print(user)
    show_test4(message)


@bot.message_handler(content_types=["text"])
def show_test4(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton("ОТВЕТ")
    btn2 = types.KeyboardButton("Ответ 2")
    btn3 = types.KeyboardButton("Ответ 3")
    btn4 = types.KeyboardButton("Ответ 4")
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    bot.send_message(message.chat.id, "Вопрос #4. <вопрос4>", reply_markup=markup)
    bot.register_next_step_handler(message, check_test4)

@bot.message_handler(content_types=["text"])
def check_test4(message):
    user_id = message.from_user.id
    user_answer = message.text
    user = users[user_id]
    correct_answer = "ОТВЕТ"
    if user_answer == correct_answer:
        user.test4 = 1
        users[user_id] = user
    show_test5(message)
    print(user)

@bot.message_handler(content_types=["text"])
def show_test5(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton("ОТВЕТ")
    btn2 = types.KeyboardButton("Ответ 2")
    btn3 = types.KeyboardButton("Ответ 3")
    btn4 = types.KeyboardButton("Ответ 4")
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    bot.send_message(message.chat.id, "Вопрос #5. <вопрос5>", reply_markup=markup)
    bot.register_next_step_handler(message, check_test5)

@bot.message_handler(content_types=["text"])
def check_test5(message):
    user_id = message.from_user.id
    user_answer = message.text
    user = users[user_id]
    correct_answer = "ОТВЕТ"
    if user_answer == correct_answer:
        user.test5 = 1
        users[user_id] = user
    print(user)
    final(message)

def final(message):
    ''' В РАЗРАБОТКЕ'''
    bot.send_message(message.chat.id, "Тест пройден")
    os.abort()






if __name__ == "__main__":
    bot.infinity_polling()
