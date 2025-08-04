from aiogram import Router
from .start import router as start_router
from .read_text import router as read_text
from .learn_language import router as learn_lang



router = Router()
router.include_router(learn_lang)
router.include_router(start_router)
router.include_router(read_text)


