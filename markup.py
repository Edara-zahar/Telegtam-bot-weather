from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btnStart = KeyboardButton('/start')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnStart)