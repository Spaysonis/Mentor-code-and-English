from aiogram import Router
from aiogram.types import Message, CallbackQuery
from BotTelegram.state.State import UserStates
from aiogram.fsm.context import FSMContext
from Gemi.question_generator import create_question
from BotTelegram.random_word.word_random import random_names
import asyncio
from BotTelegram.keyboard.keyboard import back_menu as kb_back
from BotTelegram.keyboard.keyboard import main_menu as kb_main
router = Router()


@router.callback_query(lambda c: c.data== 'read_text')
async def handle_read_text(callback: CallbackQuery, state:FSMContext):

    """THIS FUNCTION ACCEPT TEXT FROM THE USER"""

    await state.set_state(UserStates.waiting_for_text)
    await callback.message.answer(f"{random_names()}", reply_markup=kb_back)
    await callback.answer()


@router.message(UserStates.waiting_for_text)
async def receive_text(message:Message, state:FSMContext):


    """THIS FUNCTION TRANSMITS THE TEXT USER IN AI AND RETURN QUESTIONS"""
    try:

        user_text = message.text # user text
        questions = create_question(user_text) # post user text to Ai


        await message.answer(f"Вот вопросы по твоему тексту:\n\n{questions}")
        await message.answer(text='Предоставь мне ответы и я проверю их', reply_markup=kb_back)
        await state.update_data(
            original_text=user_text,
            generated_questions=questions
        )
        await state.set_state(UserStates.waiting_for_answers)
        await asyncio.sleep(2)
        await message.delete()


    except Exception as e:
        await message.answer(f"⚠️ Ошибка при обработке текста {e}")
        await state.clear()


@router.message(UserStates.waiting_for_answers)
async def check_answer(message: Message, state:FSMContext):

    """THIS FUNCTION TRANSMIT ANSWER, TEXT, QUESTION IN AI AND CHEK RESULT"""

    data = await state.get_data()
    answer_text = message.text
    original_text = data.get('original_text')
    question = data.get('generated_questions')

    result = create_question(original_text, question, answer_text)

    await message.answer(result, reply_markup=kb_main)
    await state.clear()






@router.callback_query(lambda c: c.data=='back')
async def return_to_back(callback: CallbackQuery, state:FSMContext):
    await callback.message.answer('Выберите действие:', reply_markup=kb_main)

    await state.clear()
    await callback.answer()