from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router

from BotTelegram.keyboard.keyboard import main_menu as kb_main




router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Выберите действие:', reply_markup=kb_main)


