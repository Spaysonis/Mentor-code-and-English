from aiogram import Router

router = Router()
from Gemi.question_generator import create_new_word
from aiogram.types import Message, CallbackQuery
from BotTelegram.state.State import UserStates
from aiogram.fsm.context import FSMContext

from BotTelegram.keyboard.keyboard import learn_menu as ln_kb

@router.callback_query(lambda c: c.data=='learn_new_words')
async def repeat_word(callback: CallbackQuery):
    await callback.message.answer('Привет! Что ты хочешь сделать?!', reply_markup=ln_kb)
    await callback.answer()


@router.callback_query(lambda c: c.data=='learn_new_word')
async def learn_new_word(callback: CallbackQuery):
    five_word = create_new_word()
    await callback.message.answer(five_word)
