from aiogram import Router
from .start import router as start_router
from .read_text import router as read_text



router = Router()
router.include_router(start_router)
router.include_router(read_text)


