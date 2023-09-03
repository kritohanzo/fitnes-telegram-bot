from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

kb = ReplyKeyboardMarkup(one_time_keyboard=True)
kb.add(KeyboardButton("Поделиться номером", request_contact=True))

user_buttons = ReplyKeyboardMarkup(one_time_keyboard=True)
user_buttons.add(KeyboardButton("Посмотреть все рассылки"))

admin_buttons = ReplyKeyboardMarkup(one_time_keyboard=True)
admin_buttons.add(KeyboardButton("Добавить новую рассылку"))
admin_buttons.add(KeyboardButton("Посмотреть существующие рассылки"))
admin_buttons.add(KeyboardButton("Назначить администратора"))
admin_buttons.add(KeyboardButton("Разжаловать администратора"))

to_start = ReplyKeyboardMarkup(one_time_keyboard=True)
to_start.add(KeyboardButton("В главное меню"))

spam_variables = InlineKeyboardMarkup()
spam_variables.add(InlineKeyboardButton("Удалить рассылку", callback_data="delete_spam_1"))
spam_variables.add(InlineKeyboardButton("Закончить предподписку и объявить об открытии", callback_data="stop_spam_1"))

delete_spam_button = InlineKeyboardMarkup()
delete_spam_button.add(InlineKeyboardButton("Да, я уверен, что хочу удалить рассылку", callback_data="delete_spam_2"))
delete_spam_button.add(InlineKeyboardButton("Закончить предподписку и объявить об открытии", callback_data="stop_spam_1"))

stop_spam_button = InlineKeyboardMarkup()
stop_spam_button.add(InlineKeyboardButton("Удалить рассылку", callback_data="delete_spam_1"))
stop_spam_button.add(InlineKeyboardButton("Да, я уверен, что хочу закончить предподписку и объявить об открытии", callback_data="stop_spam_2"))

subscribe_spam = InlineKeyboardMarkup()
subscribe_spam.add(InlineKeyboardButton("Подписаться на рассылку", callback_data="subscribe_spam"))

unsubscribe_spam = InlineKeyboardMarkup()
unsubscribe_spam.add(InlineKeyboardButton("Отписаться от рассылки", callback_data="unsubscribe_spam"))

redirect_to_spam = InlineKeyboardMarkup()
redirect_to_spam.add(InlineKeyboardButton("ПЕРЕЙТИ К ПРОДУКТУ", callback_data="redirect_to_spam"))