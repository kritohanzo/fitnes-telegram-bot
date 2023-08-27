from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

kb = ReplyKeyboardMarkup(one_time_keyboard=True)
kb.add(KeyboardButton("Поделиться номером", request_contact=True))

user_buttons = ReplyKeyboardMarkup(one_time_keyboard=True)
user_buttons.add(KeyboardButton("Подписаться на рассылку"))

admin_buttons = ReplyKeyboardMarkup(one_time_keyboard=True)
admin_buttons.add(KeyboardButton("Добавить новую рассылку"))
admin_buttons.add(KeyboardButton("Удалить существующую рассылку"))
admin_buttons.add(KeyboardButton("Назначить администратора"))
admin_buttons.add(KeyboardButton("Разжаловать администратора"))

to_start = ReplyKeyboardMarkup(one_time_keyboard=True)
to_start.add(KeyboardButton("В главное меню"))

delete_spam_button = InlineKeyboardMarkup()
delete_spam_button.add(InlineKeyboardButton("Удалить рассылку", callback_data="delete_spam"))