from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from get_username import *

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
	username = getUsername(message.from_user)
	await message.answer(f'Hello, {username} 👋')