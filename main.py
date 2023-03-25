import telebot

# Токен доступа HTTP API
TOKEN = '6188116645:AAEwkfEEANinxKl7iGYhbhEU4GCvab7MwDE'

# Создание экземпляра бота
bot = telebot.TeleBot(TOKEN)

# Вопросы и ответы викторины
questions = {
    "Какая столица Украины?": ["Киев", "Москва", "Лондон"],
    "Какая самая высокая гора в Украине?": ["Говерла", "Эверест", "Эльбрус"],
    "Какая река является самой длинной в Украине?": ["Днепр", "Волга", "Дунай"],
    "В каком году Украина получила независимость?": ["1991", "1989", "1993"],
    "Какое море находится у берегов Украины?": ["Черное", "Каспийское", "Азовское"]
}

# Клавиатура для вариантов ответов
keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

# Добавляем кнопки на клавиатуру
for question in questions:
    keyboard.add(*[telebot.types.KeyboardButton(answer) for answer in questions[question]])
    keyboard.add(*[telebot.types.KeyboardButton(answer) for answer in questions[question]])

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # Приветственное сообщение и инструкция к викторине
    bot.reply_to(message, "Привет! Я бот-викторина. Я задам тебе пять вопросов о Украине. Выбери правильный ответ из вариантов, используя клавиатуру.", reply_markup=keyboard)

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def quiz(message):
    # Поиск вопроса в словаре
    for question in questions:
        if message.text in questions[question]:
            # Если ответ правильный, отправляем поздравление
            if message.text == question[0]:
                bot.reply_to(message, "Правильно! Поздравляю!")
            # Если ответ неправильный, отправляем коррекцию
            else:
                bot.reply_to(message, "Неправильно. Правильный ответ: {}".format(question[0]))
            # Удаляем вопрос из словаря, чтобы он не задавался повторно
            del questions[question]
            break
    # Проверяем, остались ли еще вопросы в словаре
    if not questions:
        bot.reply_to(message, "Вопросы закончились. Спасибо за участие!")
    else:
        # Если еще остались вопросы, задаем следующий вопрос
        next_question = list(questions.keys())[0]
        bot.reply_to(message, next_question, reply_markup=keyboard)