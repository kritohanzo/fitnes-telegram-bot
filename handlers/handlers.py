from aiogram.types import Rout
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.user_keyboard import get_start_buttons


router = Router()



@router.message(Command("start"))  # [2]
async def cmd_start(message: Message):
    await message.answer(
        "Привет, я бот, который может смотреть ваше расписание "
        "и сопоставлять его с расписанием ваших друзей. "
        "Благодаря мне, вы сможете узнать, когда вам с друзьями "
        "будет удобно встретиться после или между пар!\n\n"
        "Если вы заметите какие-то баги - обратитесь "
        "к разработчику бота «@kritohanzo»\n\n"
        "Чтобы начать пользоваться мной - вам нужно указать "
        "своё ФИО. Его можно будет удалить в любой момент.",
        reply_markup=get_start_buttons(),
    )
