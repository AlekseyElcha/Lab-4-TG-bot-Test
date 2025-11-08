# pip install telebot==0.0.5
# pip install dataclasses==0.8
from telebot import *
from time import sleep
from dataclasses import dataclass
from random import shuffle
from datetime import datetime

@dataclass
class User:
    name: str
    tg_id: int
    tg_username: str
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

    def sum_points(self) -> int:
        return self.test1 + self.test2 + self.test3 + self.test4 + self.test5

    def time_spent_on_test(self) -> str:
        return str(self.end_time - self.start_time)[:-7]

    def calculate_percentage(self) -> int:
        return round(self.sum_points()/questions_count * 100)

    def create_result_message(self) -> str:
        if self.calculate_percentage() == 100:
            result_message = "Вау! Максимум!!! Поздавляем с успешным освеоением материала!"
        elif self.calculate_percentage() > 75:
            result_message = "Хороший результат! Высокий уровень осознания материала! Так держать!"
        elif self.calculate_percentage() <= 75 and self.calculate_percentage() > 50:
            result_message = "Неплохо! Ошибки есть, но это поправимо. Советуем ещё внимательно изучить теорию, знания лишними не бывают:)"
        elif self.calculate_percentage() > 20 and self.calculate_percentage() <= 50:
            result_message = "Что-то правильно - это уже хорошо, но, пожалуйста, подробнее изучите наши материалы!"
        else:
            result_message = "Маловато баллов... Но если поработать с нашими материалами, низкий балл останется в прошлом!"
        return result_message


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

bot = TeleBot("", skip_pending=True)
group_id = -5078749266

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
    var = [1, 2, 3, 4, 5]
    shuffle(var)
    t0 = datetime.today()
    user = User(
        name=replace_decode(message.text), tg_id=message.from_user.id, tg_username=message.from_user.username,
        test1=0, test2=0, test3=0, test4=0, test5=0,
        question1=var[0], question2=var[1], question3=var[2], question4=var[3], question5=var[4], start_time=t0, end_time=t0
    )
    users[message.from_user.id] = user
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
        bot.send_message(message.chat.id, "Правильно!")
        try:
            with open(r"C:\Users\alesh\Downloads\CorrectAnimatedSticker.tgs", 'rb') as anim:
                sticker_msg = bot.send_sticker(message.chat.id, anim)
                sleep(1.25)
                bot.delete_message(message.chat.id, sticker_msg.message_id)
        except:
            print("Ошибка при отправке стикера")
    else:
        bot.send_message(message.chat.id, "Ответ неверный, к сожалению:(")
        try:
            with open(r"C:\Users\alesh\Downloads\IncorrectAnimatedSticker.tgs", 'rb') as anim:
                sticker_msg = bot.send_sticker(message.chat.id, anim)
                sleep(1.25)
                bot.delete_message(message.chat.id, sticker_msg.message_id)
        except:
            print("Ошибка при отправке стикера")
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
    bot.send_message(message.chat.id, "#2. " + question.quest, reply_markup=markup)
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
        bot.send_message(message.chat.id, "Верно!")
        user.test2 = 1
        users[user_id] = user
        try:
            with open(r"C:\Users\alesh\Downloads\CorrectAnimatedSticker.tgs", 'rb') as anim:
                sticker_msg = bot.send_sticker(message.chat.id, anim)
                sleep(1.25)
                bot.delete_message(message.chat.id, sticker_msg.message_id)
        except:
            print("Ошибка при отправке стикера")
    else:
        bot.send_message(message.chat.id, "Неправильно:(")
        try:
            with open(r"C:\Users\alesh\Downloads\IncorrectAnimatedSticker.tgs", 'rb') as anim:
                sticker_msg = bot.send_sticker(message.chat.id, anim)
                sleep(1.25)
                bot.delete_message(message.chat.id, sticker_msg.message_id)
        except:
            print("Ошибка при отправке стикера")
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
        try:
            with open(r"C:\Users\alesh\Downloads\CorrectAnimatedSticker.tgs", 'rb') as anim:
                sticker_msg = bot.send_sticker(message.chat.id, anim)
                sleep(1.25)
                bot.delete_message(message.chat.id, sticker_msg.message_id)
        except:
            print("Ошибка при отправке стикера")
    else:
        bot.send_message(message.chat.id, "Эх, ошибка...")
        try:
            with open(r"C:\Users\alesh\Downloads\IncorrectAnimatedSticker.tgs", 'rb') as anim:
                sticker_msg = bot.send_sticker(message.chat.id, anim)
                sleep(1.25)
                bot.delete_message(message.chat.id, sticker_msg.message_id)
        except:
            print("Ошибка при отправке стикера")
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
        try:
            with open(r"C:\Users\alesh\Downloads\CorrectAnimatedSticker.tgs", 'rb') as anim:
                sticker_msg = bot.send_sticker(message.chat.id, anim)
                sleep(1.25)
                bot.delete_message(message.chat.id, sticker_msg.message_id)
        except:
            print("Ошибка при отправке стикера")
    else:
        bot.send_message(message.chat.id, "Неа, неверно...")
        try:
            with open(r"C:\Users\alesh\Downloads\IncorrectAnimatedSticker.tgs", 'rb') as anim:
                sticker_msg = bot.send_sticker(message.chat.id, anim)
                sleep(1.25)
                bot.delete_message(message.chat.id, sticker_msg.message_id)
        except:
            print("Ошибка при отправке стикера")
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
        try:
            with open(r"C:\Users\alesh\Downloads\CorrectAnimatedSticker.tgs", 'rb') as anim:
                sticker_msg = bot.send_sticker(message.chat.id, anim)
                sleep(1.25)
                bot.delete_message(message.chat.id, sticker_msg.message_id)
        except:
            print("Ошибка при отправке стикера")
    else:
        bot.send_message(message.chat.id, "Неправильный ответ:(")
        try:
            with open(r"C:\Users\alesh\Downloads\IncorrectAnimatedSticker.tgs", 'rb') as anim:
                sticker_msg = bot.send_sticker(message.chat.id, anim)
                sleep(1.25)
                bot.delete_message(message.chat.id, sticker_msg.message_id)
        except:
            print("Ошибка при отправке стикера")
    print(user)
    result(message)

def result(message):
    global questions_count, group_id
    user_id = message.from_user.id
    user = users[user_id]
    t1 = datetime.today()
    users[user_id].end_time = t1
    bot.send_message(message.chat.id, f"Тест пройден!\n"
                    f"\nНабрано {user.sum_points()}/{questions_count} ({user.calculate_percentage()}%)\n"
                    f"Затраченное время: {user.time_spent_on_test()}\n\n"
                    f"{user.create_result_message()}\n\n"
                    f"Для повторного прохождения нажмите /start",
                     reply_markup=types.ReplyKeyboardRemove())

    print(f"{user_id}, Тест пройден! Сумма баллов - {user.sum_points}")
    bot.send_message(group_id, f"Информация о прохожждении теста\n"
                               f"--------------------------------------\n"
                               f"*Ник пользователя*: {user.name}\n"
                               f"*Username*: {user.username}\n"
                               f"*ID*: {user.tg_id}\n"
                               f"--------------------------------------\n"
                               f"*Суммарный результат:* {user.sum_points()}/{questions_count}\n"
                               f"*Процент выполнения теста:* {user.calculate_percentage()}%\n"
                               f"*Затраченное время:* {user.time_spent_on_test()}\n"
                               f"--------------------------------------\n"
                               f"*Подробная статистика по каждому ответу:*\n"
                               f"*Вопрос #1:* {user.test1}\n"
                               f"*Вопрос #2:* {user.test2}\n"
                               f"*Вопрос #3:* {user.test3}\n"
                               f"*Вопрос #4:* {user.test4}\n"
                               f"*Вопрос #5:* {user.test5}\n", parse_mode="Markdown"
                     )
    del user


if __name__ == "__main__":
    bot.infinity_polling()
