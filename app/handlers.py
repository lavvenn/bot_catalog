from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

START_TEXT = """
hello
"""


@router.message(Command('start'))
async def start_command(message: Message):
    await message.answer(text = START_TEXT)

