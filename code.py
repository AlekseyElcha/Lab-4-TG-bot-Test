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
    test6: int
    test7: int
    test8: int
    test9: int
    test10: int
    test11: int
    test12: int
    test13: int
    test14: int
    test15: int
    question1: int
    question2: int
    question3: int
    question4: int
    question5: int
    question6: int
    question7: int
    question8: int
    question9: int
    question10: int
    question11: int
    question12: int
    question13: int
    question14: int
    question15: int
    start_time: datetime
    end_time: datetime

    def sum_points(self) -> int:
        return (self.test1 + self.test2 + self.test3 + self.test4 + self.test5 +
                self.test6 + self.test7 + self.test8 + self.test9 + self.test10 +
                self.test11 + self.test12 + self.test13 + self.test14 + self.test15)

    def time_spent_on_test(self) -> str:
        return str(self.end_time - self.start_time)[:-7]

    def calculate_percentage(self) -> int:
        return round(self.sum_points()/questions_count * 100)

    def create_result_message(self) -> str:
        if self.calculate_percentage() == 100:
            result_message = "Вау! Максимум!!! Поздравляем с успешным освеоением материала!"
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
     Question(id=1, quest="Что характерно для платных сетевых протоколов (PAID PROTOCOLS)?", var1="Бесплатное использование, открытый исходный код", var2="На текущий момент устарели и практически не применяются", var3="Разрабатываются исключительно некоммерческими организациями", var4="Для использования требуется лицензия или подписка", correct_var="Для использования требуется лицензия или подписк"),
     Question(id=2, quest="Какую метрику протокол RIP (Routing Information Protocol) использует для выбора оптимального маршрута?", var1="задержку (latency)", var2="нагрузку канала (load)", var3="ширину полосы пропускания (bandwidth)", var4="количество переходов (hop count)", correct_var="количество переходов (hop count)"),
     Question(id=3, quest="Какова основная функция протоколов резервирования каналов, таких как HSRP, VRRP и GLBP?", var1="Увеличение скорости передачи данных в сети", var2="Шифрование трафика между маршрутизаторами", var3="Защита сети от внешних атак", var4="Автоматическое переключение на резервный канал при отказе основного", correct_var="Автоматическое переключение на резервный канал при отказе основного"),
     Question(id=4, quest="Для каких целей преимущественно разрабатываются уникальные сетевые протоколы?", var1="Для замены универсальных протоколов, таких как TCP/IP, в домашних сетях", var2="Для обеспечения максимальной совместимости между оборудованием разных производителей", var3="Для упрощения настройки сетевого оборудования для обычных пользователей", var4="Для решения специальных задач в узких областях, например, в промышленных системах управления", correct_var="Для решения специальных задач в узких областях, например, в промышленных системах управления"),
     Question(id=5, quest="Какую основную функцию выполняют теговые протоколы?", var1="Ускорение передачи данных за счет сжатия данных", var2="Шифрование сетевого трафика для обеспечения конфиденциальности", var3="Резервирование отдельных каналов связи для повышения надежности", var4="Разделение трафика по виртуальным сетям с помощью меток", correct_var="Разделение трафика по виртуальным сетям с помощью меток"),
     Question(id=6, quest="Какую основную проблему решают протоколы предотвращения петель (STP - Spanning Tree Protocol)?", var1="Слишком медленную передачу данных в больших сетях", var2="Неправильную маршрутизацию пакетов между разными сетями", var3="Недостаточную пропускную способность сетевых каналов", var4="Бесконечную циркуляцию данных из-за избыточных соединений", correct_var="Бесконечную циркуляцию данных из-за избыточных соединений"),
     Question(id=7, quest="Какую основную задачу решает протокол DHCP (Dynamic Host Configuration Protocol)?", var1="Защиту сети от несанкционированного доступа", var2="Создание виртуальных частных сетей (VPN)", var3="Маршрутизацию пакетов между разными сетями", var4="Автоматическое назначение IP-адресов и параметров сети устройствам", correct_var="Автоматическое назначение IP-адресов и параметров сети устройствам"),
     Question(id=8, quest="Какую основную функцию выполняет NAT (Network Address Translation)?", var1="Ускорение передачи данных между устройствами в локальной сети", var2="Шифрование интернет-трафика для обеспечения безопасности", var3="Автоматическое назначение IP-адресов новым устройствам", var4="Преобразование внутренних частных IP-адресов в публичные", correct_var="Преобразование внутренних частных IP-адресов в публичные"),
     Question(id=9, quest="Какую основную функцию выполняет Active Directory (AD) в корпоративной сети?", var1="Автоматическое резервное копирование данных пользователей сети", var2="Защиту сети от вирусов и вредоносных программ", var3="Организацию видеоконференций между сотрудниками", var4="Централизованное управление пользователями, компьютерами и правами доступа", correct_var="Централизованное управление пользователями, компьютерами и правами доступа"),
     Question(id=10, quest="Какую основную функцию выполняет сетевое устройство «шлюз» (gateway)?", var1="Усиливает сигнал Wi-Fi для лучшего покрытия", var2="Защищает сеть от несанкционированного доступа", var3="Автоматически назначает IP-адреса устройствам в локальной сети", var4="Обеспечивает взаимодействие между разными сетями", correct_var="Обеспечивает взаимодействие между разными сетями"),
     Question(id=11, quest="Какую основную цель преследует создание милитаризованной зоны (DMZ) в сети?", var1="Ускорение доступа к интернету для всех пользователей внутренней сети", var2="Обеспечение анонимности трафика при работе в интернете", var3="Создание резервной копии всех данных организации", var4="Размещение публичных серверов в изолированной зоне для защиты внутренней сети", correct_var="Размещение публичных серверов в изолированной зоне для защиты внутренней сети"),
     Question(id=12, quest="Какую основную задачу решает управление DNS (системой доменных имен)?", var1="Шифрование интернет-соединений для защиты конфиденциальности", var2="Автоматическое назначение IP-адресов сетевым устройствам", var3="Фильтрацию нежелательного контента на уровне сети", var4="Настройку записей, связывающих доменные имена с IP-адресами", correct_var="Настройку записей, связывающих доменные имена с IP-адресами"),
     Question(id=13, quest="Какую основную функцию выполняет брандмауэр (firewall)?", var1="Ускорение сетевого соединения за счет кэширования данных", var2="Автоматическое исправление ошибок в передаваемых данных", var3="Преобразование доменных имен в IP-адреса", var4="Контроль и фильтрация сетевого трафика согласно правилам безопасности", correct_var="Контроль и фильтрация сетевого трафика согласно правилам безопасности"),
     Question(id=14, quest="Какова основная характеристика сети DNS (DNS Networks)?", var1="Это единый централизованный сервер для всех доменных имен", var2="Это локальная база данных на каждом компьютере пользователя", var3="Это протокол для автоматического назначения IP-адресов", var4="Это система взаимосвязанных серверов по всему миру", correct_var="Это система взаимосвязанных серверов по всему миру"),
     Question(id=15, quest="Какое ключевое преимущество предоставляет пользователям система DNS?", var1="Автоматическое шифрование всех интернет-соединений", var2="Увеличение скорости загрузки веб-страниц", var3="Бесплатное создание доменных имен", var4="Возможность не запоминать числовые IP-адреса сайтов", correct_var="Возможность не запоминать числовые IP-адреса сайтов"),
]
questions_count = 15

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
    var = [i for i in range(1, 16)]
    shuffle(var)
    t0 = datetime.today()
    user = User(
        name=replace_decode(message.text), tg_id=message.from_user.id, tg_username=message.from_user.username,
        test1=0, test2=0, test3=0, test4=0, test5=0, test6=0, test7=0, test8=0,
        test9=0, test10=0, test11=0, test12=0, test13=0, test14=0, test15=0,
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
    question_id = users[user_id].question3
    question = questions[question_id - 1]
    correct_answer = replace_decode(question.correct_var)
    if user_answer == correct_answer:
        user.test5 = 1
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
    show_test6(message)


@bot.message_handler(content_types=["text"])
def show_test6(message):
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
    bot.send_message(message.chat.id, "#6. " + question.quest, reply_markup=markup)
    bot.register_next_step_handler(message, check_test6)

@bot.message_handler(content_types=["text"])
def check_test6(message):
    user_id = message.from_user.id
    user = users[user_id]
    user_answer = replace_decode(message.text)
    question_id = users[user_id].question3
    question = questions[question_id - 1]
    correct_answer = replace_decode(question.correct_var)
    if user_answer == correct_answer:
        user.test6 = 1
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
    show_test7(message)


@bot.message_handler(content_types=["text"])
def show_test7(message):
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
    bot.send_message(message.chat.id, "#7. " + question.quest, reply_markup=markup)
    bot.register_next_step_handler(message, check_test7)

@bot.message_handler(content_types=["text"])
def check_test7(message):
    user_id = message.from_user.id
    user = users[user_id]
    user_answer = replace_decode(message.text)
    question_id = users[user_id].question3
    question = questions[question_id - 1]
    correct_answer = replace_decode(question.correct_var)
    if user_answer == correct_answer:
        user.test7 = 1
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
    show_test8(message)

@bot.message_handler(content_types=["text"])
def show_test8(message):
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
    bot.send_message(message.chat.id, "#8. " + question.quest, reply_markup=markup)
    bot.register_next_step_handler(message, check_test8)

@bot.message_handler(content_types=["text"])
def check_test8(message):
    user_id = message.from_user.id
    user = users[user_id]
    user_answer = replace_decode(message.text)
    question_id = users[user_id].question3
    question = questions[question_id - 1]
    correct_answer = replace_decode(question.correct_var)
    if user_answer == correct_answer:
        user.test8 = 1
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
    show_test9(message)

@bot.message_handler(content_types=["text"])
def show_test9(message):
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
    bot.send_message(message.chat.id, "#9. " + question.quest, reply_markup=markup)
    bot.register_next_step_handler(message, check_test9)

@bot.message_handler(content_types=["text"])
def check_test9(message):
    user_id = message.from_user.id
    user = users[user_id]
    user_answer = replace_decode(message.text)
    question_id = users[user_id].question3
    question = questions[question_id - 1]
    correct_answer = replace_decode(question.correct_var)
    if user_answer == correct_answer:
        user.test9 = 1
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
    show_test10(message)

@bot.message_handler(content_types=["text"])
def show_test10(message):
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
    bot.send_message(message.chat.id, "#10. " + question.quest, reply_markup=markup)
    bot.register_next_step_handler(message, check_test10)

@bot.message_handler(content_types=["text"])
def check_test10(message):
    user_id = message.from_user.id
    user = users[user_id]
    user_answer = replace_decode(message.text)
    question_id = users[user_id].question3
    question = questions[question_id - 1]
    correct_answer = replace_decode(question.correct_var)
    if user_answer == correct_answer:
        user.test10 = 1
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
    show_test11(message)

@bot.message_handler(content_types=["text"])
def show_test11(message):
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
    bot.send_message(message.chat.id, "#11. " + question.quest, reply_markup=markup)
    bot.register_next_step_handler(message, check_test11)

@bot.message_handler(content_types=["text"])
def check_test11(message):
    user_id = message.from_user.id
    user = users[user_id]
    user_answer = replace_decode(message.text)
    question_id = users[user_id].question3
    question = questions[question_id - 1]
    correct_answer = replace_decode(question.correct_var)
    if user_answer == correct_answer:
        user.test11 = 1
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
    show_test12(message)

@bot.message_handler(content_types=["text"])
def show_test12(message):
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
    bot.send_message(message.chat.id, "#12. " + question.quest, reply_markup=markup)
    bot.register_next_step_handler(message, check_test12)

@bot.message_handler(content_types=["text"])
def check_test12(message):
    user_id = message.from_user.id
    user = users[user_id]
    user_answer = replace_decode(message.text)
    question_id = users[user_id].question3
    question = questions[question_id - 1]
    correct_answer = replace_decode(question.correct_var)
    if user_answer == correct_answer:
        user.test12 = 1
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
    show_test13(message)

@bot.message_handler(content_types=["text"])
def show_test13(message):
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
    bot.send_message(message.chat.id, "#13. " + question.quest, reply_markup=markup)
    bot.register_next_step_handler(message, check_test13)

@bot.message_handler(content_types=["text"])
def check_test13(message):
    user_id = message.from_user.id
    user = users[user_id]
    user_answer = replace_decode(message.text)
    question_id = users[user_id].question3
    question = questions[question_id - 1]
    correct_answer = replace_decode(question.correct_var)
    if user_answer == correct_answer:
        user.test13 = 1
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
    show_test14(message)

@bot.message_handler(content_types=["text"])
def show_test14(message):
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
    bot.send_message(message.chat.id, "#14. " + question.quest, reply_markup=markup)
    bot.register_next_step_handler(message, check_test14)

@bot.message_handler(content_types=["text"])
def check_test14(message):
    user_id = message.from_user.id
    user = users[user_id]
    user_answer = replace_decode(message.text)
    question_id = users[user_id].question3
    question = questions[question_id - 1]
    correct_answer = replace_decode(question.correct_var)
    if user_answer == correct_answer:
        user.test14 = 1
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
    show_test15(message)

@bot.message_handler(content_types=["text"])
def show_test15(message):
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
    bot.send_message(message.chat.id, "#15. " + question.quest, reply_markup=markup)
    bot.register_next_step_handler(message, check_test15)

@bot.message_handler(content_types=["text"])
def check_test15(message):
    user_id = message.from_user.id
    user = users[user_id]
    user_answer = replace_decode(message.text)
    question_id = users[user_id].question5
    question = questions[question_id - 1]
    correct_answer = replace_decode(question.correct_var)
    if user_answer == correct_answer:
        user.test15 = 1
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
                               f"*Вопрос #4:* {user.test5}\n"
                               f"*Вопрос #4:* {user.test6}\n"
                               f"*Вопрос #4:* {user.test7}\n"
                               f"*Вопрос #4:* {user.test8}\n"
                               f"*Вопрос #4:* {user.test9}\n"
                               f"*Вопрос #4:* {user.test10}\n"
                               f"*Вопрос #4:* {user.test11}\n"
                               f"*Вопрос #4:* {user.test12}\n"
                               f"*Вопрос #4:* {user.test13}\n"
                               f"*Вопрос #4:* {user.test14}\n"
                               f"*Вопрос #5:* {user.test15}\n", parse_mode="Markdown"
                     )
    del user


if __name__ == "__main__":
    bot.infinity_polling()
