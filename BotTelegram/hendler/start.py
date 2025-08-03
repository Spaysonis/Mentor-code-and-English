from aiogram.filters import CommandStart


from BotTelegram.keyboard.keyboard import main_menu as kb_main



from aiogram.types import Message
from aiogram import Router

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Выберите действие:', reply_markup=kb_main)


