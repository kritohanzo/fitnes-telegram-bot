from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv
from aiogram.types import InputMediaPhoto
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ContentType
# from handlers import singup, work
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from db.models import User, Spam
from db import Database as db
from utils.states import Registation, UserMenu, AdminMenu
from utils.keyboards import kb, user_buttons, admin_buttons, to_start, delete_spam_button_1, delete_spam_button_2


load_dotenv()
bot = Bot(os.getenv("TELEGRAM_TOKEN"))
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=["start"])
async def start_command(message):
    user = db.get(User, telegram_id=message.from_user.id)
    if user and user[0].is_admin:
        await AdminMenu.intro.set()
        await bot.send_message(message.from_user.id, f"Привет, {user[0].name}, что делаем на этот раз?", reply_markup=admin_buttons)
    elif user:
        # await Dialog.user_menu.set()
        await bot.send_message(message.from_user.id, f"Привет, {user[0].name}, что делаем на этот раз?", reply_markup=user_buttons)
    else:
        await Registation.intro.set()
        await bot.send_message(message.from_user.id, "Поделись номером, чтобы мы могли добавить тебя в нашу базу", reply_markup=kb)

@dp.message_handler(content_types=ContentType.CONTACT, state=Registation.intro)
async def get_contact(message, state):
    await Registation.intro.set_contact(message.contact.phone_number)
    await message.answer("Так же нам нужно ваше имя, чтобы знать, как к вам обращаться")

@dp.message_handler(state=Registation.intro)
async def registration_user(message, state):
    name = message.text
    contact = await Registation.intro.get_contact()
    telegram_id = message.from_user.id
    new_user = User(name=name, contact=contact, telegram_id=telegram_id, is_admin=True)
    db.create(new_user)
    await state.finish()
    await bot.send_message(message.from_user.id, "Спасибо за регистрацию!")

@dp.message_handler(lambda message: message.text == "В главное меню", state=AdminMenu)
async def return_to_start(message, state):
    await state.finish()
    await start_command(message)

@dp.message_handler(state=AdminMenu.intro)
async def process_admin_menu(message):
    if message.text == "Добавить новую рассылку":
        await AdminMenu.add_spam.set()
        await bot.send_message(message.from_user.id, "Прикрепите картинку и текст к сообщению для создания новой рассылки", reply_markup=to_start)
    
    elif message.text == "Удалить существующую рассылку":
        await AdminMenu.delete_spam.set()
        spams = db.get(Spam)
        
        if spams:
            for spam in spams:
                await bot.send_photo(message.from_user.id, spam.picture_telegram_id, spam.text, reply_markup=delete_spam_button_1)
            await bot.send_message(message.from_user.id, "Нажмите на кнопочку под какой-то рассылкой, чтобы удалить её навсегда", reply_markup=to_start)
        else:
            await bot.send_message(message.from_user.id, "Нет активных рассылок")
            await start_command(message)

    elif message.text == "Назначить администратора":
        await AdminMenu.add_administrator.set()
        await bot.send_message(message.from_user.id, "Введите ID пользователя, которого вы хотите сделать администратором", reply_markup=to_start)
    
    elif message.text == "Разжаловать администратора":
        await AdminMenu.delete_administrator.set()
        await bot.send_message(message.from_user.id, "Введите ID пользователя, у которого вы хотите отобрать админку", reply_markup=to_start)
    
    else:
        await bot.send_message(message.from_user.id, "Выберите команду из доступной клавиатуры", reply_markup=admin_buttons)

@dp.message_handler(state=AdminMenu.add_spam, content_types=[ContentType.PHOTO, ContentType.TEXT])
async def process_add_spam(message, state):
    error_message = "Сообщение обязательно должно содержать только одну картинку и текст к ней."
    if not message.photo or not message.caption:
        await bot.send_message(message.from_user.id, error_message)
    else:
        new_spam = Spam(text=message.caption, picture_telegram_id=message.photo[-1].file_id)
        db.create(new_spam)
        await AdminMenu.intro.set()
        await bot.send_message(message.from_user.id, "Новая рассылка успешно добавлена", reply_markup=admin_buttons)

@dp.callback_query_handler(lambda c: c.data == "delete_spam_1", state=AdminMenu.delete_spam)
async def process_callback_button1(callback_query, state):
    await callback_query.message.edit_caption(caption="Вы уверены, что хотите удалить эту рассылку?", reply_markup=delete_spam_button_2)

@dp.callback_query_handler(lambda c: c.data == "delete_spam_2", state=AdminMenu.delete_spam)
async def process_callback_button1(callback_query, state):
    text = callback_query.message.caption
    # picture_telegram_id = callback_query.message.photo[-1].file_id
    # print(picture_telegram_id)
    spam = db.get(Spam, text=text)
    # db.delete(spam[0])
    await callback_query.message.edit_caption(caption="Рассылка успешно удалена")

@dp.message_handler()
async def echo(message):
    await start_command(message)



if __name__ == "__main__":
    db.check_exists_db()
    executor.start_polling(dp)