from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='📖 Прочесть текст и ответить на вопросы', callback_data='read_text')],
     [InlineKeyboardButton(text='🧠 Хочу прокачать Английский', callback_data='learn_new_words')]
])



back_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вернуться назад', callback_data='back')]
])


