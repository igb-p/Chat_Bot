from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

#память для запоминания состояний
storage = MemoryStorage()
#токен бота
bot = Bot (token = '6032787190:AAES_W-m4UPYagBAUaj4l1eWcIc7_BY_kmA')
dp = Dispatcher(bot, storage=storage)
