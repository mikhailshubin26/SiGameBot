from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from get_username import *

import app.keyboards as kb # Import Keyboard from keyboards.py

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
	username = getUsername(message.from_user)
	await message.reply(f'Hello, {username} 👋',
		reply_markup=kb.main)

@router.message(lambda message: message.text == '⚙️ Settings')
async def settings_handler(message: Message):
    await message.answer("Here you can change your settings",
    	reply_markup=kb.settings)

# Обработчик для callback_query на кнопки настроек
@router.callback_query(lambda c: c.data == 'show_languages')
async def show_languages_handler(callback: CallbackQuery):
	await callback.message.edit_text("Choose your language:", reply_markup=kb.languages)
	await callback.answer()

@router.callback_query(lambda c: c.data == 'back_to_settings')
async def back_to_settings_handler(callback: CallbackQuery):
	await callback.message.edit_text("Here you can change your settings", reply_markup=kb.settings)
	await callback.answer()

@router.callback_query(lambda c: c.data in ['lang_en', 'lang_ru'])
async def language_chosen_handler(callback: CallbackQuery):
	lang = 'English' if callback.data == 'lang_en' else 'Русский'
	await callback.answer(text=f"You chose: {lang}", show_alert=True)
	# Здесь можно сохранить выбор языка, если нужно


	