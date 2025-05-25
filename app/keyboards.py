from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
						   InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[
	[KeyboardButton(text='👤 Play Single'), KeyboardButton(text='👥 Play with Friends')],
	[KeyboardButton(text='⚙️ Settings')]
],
	resize_keyboard=True)

settings = InlineKeyboardMarkup(inline_keyboard=[
	[InlineKeyboardButton(text='🌍 Language', callback_data="show_languages"),
	InlineKeyboardButton(text='📐 Button Size', callback_data="show_button_size")]
])

languages = InlineKeyboardMarkup(inline_keyboard=[
	[InlineKeyboardButton(text='🇬🇧 English', callback_data="lang_en"),
	InlineKeyboardButton(text='🇷🇺 Русский', callback_data="lang_ru")],
	[InlineKeyboardButton(text='⬅️', callback_data="back_to_settings")]
])