from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

#память для запоминания состояний
storage = MemoryStorage()
#токен бота
bot = Bot (token = '6222925933:AAF605khU7qscFE9hacs5c9alocyOCA61FI')
dp = Dispatcher(bot, storage=storage)
