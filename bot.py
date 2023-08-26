from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv
# from handlers import singup, work
import os
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from keyboards import start_buttons


load_dotenv()
bot_token = os.getenv("TELEGRAM_TOKEN")
bot = Bot(bot_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class Dialog(StatesGroup):
    registration = State()


@dp.message_handler(commands=["start"])
async def start_command(message):
    text = "привет привет укажи фио и телефон пжпж"
    await Dialog.registration.set()
    await bot.send_message(message.from_user.id, text)

@dp.message_handler(state=Dialog.registration)
async def registration_user(message, state):
    if message.text == "ABOBA":
        await state.finish()
        await message.answer("спасибо за регистрацию")
    else:
        await message.answer("это не правильно!")

@dp.message_handler()
async def echo(message):
    await message.reply('ok')



if __name__ == "__main__":
    executor.start_polling(dp)