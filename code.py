# pip install telebot==0.0.5
from telebot import *
from dataclasses import *
from random import shuffle
from datetime import datetime

@dataclass
class User:
    name: str
    tg_id: int
    test1: int
    test2: int
    test3: int
    test4: int
    test5: int
    question1: int
    question2: int
    question3: int
    question4: int
    question5: int
    start_time: datetime
    end_time: datetime
    @classmethod
    def sum_point(cls, test1, test2, test3, test4, test5) -> int:
        return test1 + test2 + test3 + test4 + test5

    @classmethod
    def time_spent_on_test(cls, start_time, end_time) -> str:
        return str(end_time - start_time)[:-7]

@dataclass
class Question:
    id: int
    quest: str
    var1: str
    var2: str
    var3: str
    var4: str
    correct_var: str


users = {}
questions = [
     Question(id=1, quest="quest 1", var1="id 1 var 1", var2="id 1 ver 2", var3="id 1 var 3", var4="correct id 1 var 4", correct_var="correct id 1 var 4"),
     Question(id=2, quest="quest 2", var1="id 2 var 1", var2="id 2 ver 2", var3="id 2 var 3", var4="correct id 2 var 4", correct_var="correct id 2 var 4"),
     Question(id=3, quest="quest 3", var1="id 3 var 1", var2="id 3 ver 2", var3="id 3 var 3", var4="correct id 3 var 4", correct_var="correct id 3 var 4"),
     Question(id=4, quest="quest 4", var1="id 4 var 1", var2="id 4 ver 2", var3="id 4 var 3", var4="correct id 4 var 4", correct_var="correct id 4 var 4"),
     Question(id=5, quest="quest 5", var1="id 5 var 1", var2="id 5 ver 2", var3="id 5 var 3", var4="correct id 5 var 4", correct_var="correct id 5 var 4"),
]
questions_count = 5
bot = TeleBot("8462231489:AAEAypnU5xkumFVnCh2QiGBw7zdZJGEGvw4", skip_pending=True)

symbols = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!', '₽', '$', '#', '%']
def replace_decode(s):
    t = [i for i in s if i not in symbols]
    return ''.join(t)

@bot.message_handler(commands=["start"])
def start(m, res=False):
    global questions_count
    bot.send_message(m.chat.id, f"Добро пожаловать в тест!\n"
                                f"Перед началом выполнения, пожалуйста, прочитайте инструкцию:\n"
                                f" - Тест состоит из {questions_count} вопросов.\n"
                                f" - К каждому вопросу Вам будет дано 4 варианта ответа.\n"
                                f" - Выбор подходящего варианта ответа осуществляется КНОПКАМИ\n"
                                f" - Желаем удачи!", reply_markup=types.ReplyKeyboardRemove())
    bot.send_message(m.chat.id, "Введите, пожалуйста Ваше имя (никнейм для викторины)")
    bot.register_next_step_handler(m, get_name1)

@bot.message_handler(content_types=["text"])
def get_name1(message):
    user_id = message.from_user.id
    user_name = replace_decode(message.text)
    var = [1, 2, 3, 4, 5]
    shuffle(var)
    t0 = datetime.today()
    user = User(
        name=user_name, tg_id=user_id,
        test1=0, test2=0, test3=0, test4=0, test5=0,
        question1=var[0], question2=var[1], question3=var[2], question4=var[3], question5=var[4], start_time=t0, end_time=t0
    )
    users[user_id] = user
    bot.send_message(message.chat.id, "Отличный ник! Приступаем к тесту!")
    show_test1(message)

@bot.message_handler(content_types=["text"])
def show_test1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    user_id = message.from_user.id
    question_id = users[user_id].question1
    question = questions[question_id-1]
    variants = [question.var1, question.var2, question.var3, question.var4]
    shuffle(variants)
    btn1 = types.KeyboardButton(variants[0])
    btn2 = types.KeyboardButton(variants[1])
    btn3 = types.KeyboardButton(variants[2])
    btn4 = types.KeyboardButton(variants[3])
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    bot.send_message(message.chat.id, "#1. " + question.quest, reply_markup=markup)
    bot.register_next_step_handler(message, check_test1)

@bot.message_handler(content_types=["text"])
def check_test1(message):
    user_id = message.from_user.id
    user = users[user_id]
    user_answer = replace_decode(message.text)
    question_id = users[user_id].question1
    question = questions[question_id - 1]
    correct_answer = replace_decode(question.correct_var)
    if user_answer == correct_answer:
        user.test1 = 1
        users[user_id] = user
        bot.send_message(message.chat.id, "Верно!")
    else:
        bot.send_message(message.chat.id, "Ответ неверный, к сожалению:(")
    print(user)
    show_test2(message)


@bot.message_handler(content_types=["text"])
def show_test2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    user_id = message.from_user.id
    question_id = users[user_id].question2
    question = questions[question_id-1]
    variants = [question.var1, question.var2, question.var3, question.var4]
    shuffle(variants)
    btn1 = types.KeyboardButton(variants[0])
    btn2 = types.KeyboardButton(variants[1])
    btn3 = types.KeyboardButton(variants[2])
    btn4 = types.KeyboardButton(variants[3])
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    bot.send_message(message.chat.id, "#2. " +question.quest, reply_markup=markup)
    bot.register_next_step_handler(message, check_test2)

@bot.message_handler(content_types=["text"])
def check_test2(message):
    user_id = message.from_user.id
    user = users[user_id]
    user_answer = replace_decode(message.text)
    question_id = users[user_id].question2
    question = questions[question_id - 1]
    correct_answer = replace_decode(question.correct_var)
    if user_answer == correct_answer:
        bot.send_message(message.chat.id, "Правильно!")
        user.test2 = 1
        users[user_id] = user
    else:
        bot.send_message(message.chat.id, "Упс, ответ неверный:(")
    print(user)
    show_test3(message)


@bot.message_handler(content_types=["text"])
def show_test3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    user_id = message.from_user.id
    question_id = users[user_id].question3
    question = questions[question_id-1]
    variants = [question.var1, question.var2, question.var3, question.var4]
    shuffle(variants)
    btn1 = types.KeyboardButton(variants[0])
    btn2 = types.KeyboardButton(variants[1])
    btn3 = types.KeyboardButton(variants[2])
    btn4 = types.KeyboardButton(variants[3])
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    bot.send_message(message.chat.id, "#3. " +question.quest, reply_markup=markup)
    bot.register_next_step_handler(message, check_test3)


@bot.message_handler(content_types=["text"])
def check_test3(message):
    user_id = message.from_user.id
    user = users[user_id]
    user_answer = replace_decode(message.text)
    question_id = users[user_id].question3
    question = questions[question_id - 1]
    correct_answer = replace_decode(question.correct_var)
    if user_answer == correct_answer:
        user.test3 = 1
        users[user_id] = user
        bot.send_message(message.chat.id, "Отлично!")
    else:
        bot.send_message(message.chat.id, "Ой, ошибочка в ответе...")
    print(user)
    show_test4(message)


@bot.message_handler(content_types=["text"])
def show_test4(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    user_id = message.from_user.id
    question_id = users[user_id].question4
    question = questions[question_id-1]
    variants = [question.var1, question.var2, question.var3, question.var4]
    shuffle(variants)
    btn1 = types.KeyboardButton(variants[0])
    btn2 = types.KeyboardButton(variants[1])
    btn3 = types.KeyboardButton(variants[2])
    btn4 = types.KeyboardButton(variants[3])
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    bot.send_message(message.chat.id, "#4. " +question.quest, reply_markup=markup)
    bot.register_next_step_handler(message, check_test4)

@bot.message_handler(content_types=["text"])
def check_test4(message):
    user_id = message.from_user.id
    user = users[user_id]
    user_answer = replace_decode(message.text)
    question_id = users[user_id].question4
    question = questions[question_id - 1]
    correct_answer = replace_decode(question.correct_var)
    if user_answer == correct_answer:
        user.test4 = 1
        users[user_id] = user
        bot.send_message(message.chat.id, "Ура! Верный ответ!")
    else:
        bot.send_message(message.chat.id, "Эх, не тот вариант был выбран...")
    print(user)
    show_test5(message)

@bot.message_handler(content_types=["text"])
def show_test5(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    user_id = message.from_user.id
    question_id = users[user_id].question5
    question = questions[question_id-1]
    variants = [question.var1, question.var2, question.var3, question.var4]
    shuffle(variants)
    btn1 = types.KeyboardButton(variants[0])
    btn2 = types.KeyboardButton(variants[1])
    btn3 = types.KeyboardButton(variants[2])
    btn4 = types.KeyboardButton(variants[3])
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    bot.send_message(message.chat.id, "#5. " + question.quest, reply_markup=markup)
    bot.register_next_step_handler(message, check_test5)

@bot.message_handler(content_types=["text"])
def check_test5(message):
    user_id = message.from_user.id
    user = users[user_id]
    user_answer = replace_decode(message.text)
    question_id = users[user_id].question5
    question = questions[question_id - 1]
    correct_answer = replace_decode(question.correct_var)
    if user_answer == correct_answer:
        user.test5 = 1
        users[user_id] = user
        bot.send_message(message.chat.id, "Это успех!")
    else:
        bot.send_message(message.chat.id, "Неа, неправильно:(")
    print(user)
    result(message)

def result(message):
    global questions_count
    # DATA_FILE = open(r"C:\Users\alesh\OneDrive\Desktop\test_data.txt", "w+")
    user_id = message.from_user.id
    user = users[user_id]
    t1 = datetime.today()
    users[user_id].end_time = t1
    total_points = user.sum_point(user.test1, user.test2, user.test3, user.test4, user.test5)
    percent = total_points / questions_count * 100
    if percent > 75:
        result_message = "Отличный результат! Высокий уровень понимания темы! Так держать!"
    elif percent <= 75 and percent > 50:
        result_message = "Неплохо! Ошибки есть, но это поправимо. Советуем ещё поизучать теорию, знания лишними не бывают:)"
    elif percent > 20 and percent <= 50:
        result_message = "Что-то правильно - уже хорошо, но, пожалуйста, подробнее изучите наши материалы!"
    else:
        result_message = "Маловато баллов... Но если поработать с нашими материалами, низкий балл останется в прошлом!"
    bot.send_message(message.chat.id, f"Тест пройден!\n"
                    f"\nНабрано {total_points}/{questions_count} ({percent}%)\n"
                    f"Затраченное время: {user.time_spent_on_test(user.start_time, user.end_time)}\n\n"
                    f"{result_message}\n\n"
                    f"Для повторного прохождения нажмите /start",
                     reply_markup=types.ReplyKeyboardRemove())
    us_test1 = user.test1
    us_test2 = user.test2
    us_test3 = user.test3
    us_test4 = user.test4
    us_test5 = user.test5
    del user
    # DATA_FILE.write("User: " + str(user_id) + ", #1: " + str(us_test1) + ", #2: " + str(us_test2) + ", #3: " + str(us_test3) + ", #4: " + str(us_test4) + ", #5: " + str(us_test5) + ", sum: " + str(total_points))
    print(f"{user_id}, Тест пройден! Сумма баллов - {total_points}")
    # DATA_FILE.close()


if __name__ == "__main__":
    bot.infinity_polling()
