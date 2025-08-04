from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='📖 Прочесть текст и ответить на вопросы', callback_data='read_text')],
     [InlineKeyboardButton(text='🧠 Хочу прокачать Английский', callback_data='learn_new_words')]
])


learn_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Повторить 10 выученых слов', callback_data='repeat_word')],
    [InlineKeyboardButton(text='Выучить 5 новых слов', callback_data='learn_new_word')],
    [InlineKeyboardButton(text='Вернуться назад', callback_data='back')]
])



back_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вернуться назад', callback_data='back')]
])




