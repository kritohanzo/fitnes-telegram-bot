from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ContentType
# from handlers import singup, work
import os
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from db import Tools as db, User
# from keyboards import start_buttons


load_dotenv()
bot_token = os.getenv("TELEGRAM_TOKEN")
bot = Bot(bot_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class RegistrationState(State):
    async def set_contact(self, contact):
        self.contact = contact

    async def get_contact(self):
        return self.contact

class Dialog(StatesGroup):
    registration = RegistrationState()

kb = ReplyKeyboardMarkup(one_time_keyboard=True)
kb.add(KeyboardButton("Поделиться номером", request_contact=True))

rass = ReplyKeyboardMarkup(one_time_keyboard=True)
rass.add(KeyboardButton("Подписаться на рассылку"))

@dp.message_handler(commands=["start"])
async def start_command(message):
    user = db.get(User, telegram_id=message.from_user.id)
    print(user)
    if user:
        await bot.send_message(message.from_user.id, "Добро пожаловать в главное меню", reply_markup=rass)
    else:
        hello_text = "TIPO TEXT"
        text = "Поделись номером, чтобы мы могли добавить тебя в нашу базу"
        await Dialog.registration.set()
        await bot.send_message(message.from_user.id, hello_text)
        await bot.send_message(message.from_user.id, text, reply_markup=kb)

@dp.message_handler(content_types=ContentType.CONTACT, state=Dialog.registration)
async def get_contact(message, state):
    await Dialog.registration.set_contact(message.contact.phone_number)
    await message.answer("Так же нам нужно ваше имя, чтобы знать, как к вам обращаться")

@dp.message_handler(state=Dialog.registration)
async def registration_user(message, state):
    name = message.text
    contact = await Dialog.registration.get_contact()
    telegram_id = message.from_user.id
    new_user = User(name=name, contact=contact, telegram_id=telegram_id)
    db.create(new_user)
    await state.finish()
    await bot.send_message(message.from_user.id, "Спасибо за регистрацию!")

@dp.message_handler()
async def echo(message):
    await message.reply('ok')



if __name__ == "__main__":
    db.check_exists_db()
    executor.start_polling(dp)