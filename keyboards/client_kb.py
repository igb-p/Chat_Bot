from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1=KeyboardButton('/help')
b2=KeyboardButton('/glossary')
b3=KeyboardButton('/handbook')
b4=KeyboardButton('/vulbase')
b5=KeyboardButton('/cancel')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_base = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

# стартовая клавиатура
kb_client.row(b1, b2, b3, b4)
# клавиатура режима поиска в базе
kb_base.row(b5)
