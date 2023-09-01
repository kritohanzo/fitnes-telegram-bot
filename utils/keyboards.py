from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

kb = ReplyKeyboardMarkup(one_time_keyboard=True)
kb.add(KeyboardButton("Поделиться номером", request_contact=True))

user_buttons = ReplyKeyboardMarkup(one_time_keyboard=True)
user_buttons.add(KeyboardButton("Посмотреть рассылки"))

admin_buttons = ReplyKeyboardMarkup(one_time_keyboard=True)
admin_buttons.add(KeyboardButton("Добавить новую рассылку"))
admin_buttons.add(KeyboardButton("Удалить существующую рассылку"))
admin_buttons.add(KeyboardButton("Назначить администратора"))
admin_buttons.add(KeyboardButton("Разжаловать администратора"))

to_start = ReplyKeyboardMarkup(one_time_keyboard=True)
to_start.add(KeyboardButton("В главное меню"))

delete_spam_button_1 = InlineKeyboardMarkup()
delete_spam_button_1.add(InlineKeyboardButton("Удалить рассылку", callback_data="delete_spam_1"))

delete_spam_button_2 = InlineKeyboardMarkup()
delete_spam_button_2.add(InlineKeyboardButton("Да, я уверен, что хочу удалить рассылку", callback_data="delete_spam_2"))

subscribe_spam = InlineKeyboardMarkup()
subscribe_spam.add(InlineKeyboardButton("Подписаться на рассылку", callback_data="subscribe_spam"))

unsubscribe_spam = InlineKeyboardMarkup()
unsubscribe_spam.add(InlineKeyboardButton("Отписаться от рассылки", callback_data="unsubscribe_spam"))