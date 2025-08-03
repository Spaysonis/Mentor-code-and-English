import os
from dotenv import load_dotenv
from aiogram import Dispatcher, Bot



from aiogram.fsm.storage.memory import MemoryStorage
from BotTelegram.hendler import router

async def main():
    load_dotenv()
    token_bot = os.getenv('BOT_TOKEN')
    bot = Bot(token=token_bot)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await dp.start_polling(bot)




