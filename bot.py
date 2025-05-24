from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

import asyncio

from config import BOT_TOKEN

from get_username import getUsername

bot=Bot(token=BOT_TOKEN)
dp=Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
	username = getUsername(message.from_user)
	await message.answer(f'Hello, {username} 👋')

async def main():
	await dp.start_polling(bot)

if __name__ == '__main__':
	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		print('Exit')