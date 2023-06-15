import asyncio
from aiogram.utils import executor
from aiogram import types
from create_bot import dp
from data_base import db_open 

#async def startup(_):
 #   sqllite_db.sql_start()

if __name__ == '__main__':
    db_open.sql_start()
    from handlers import menu, text
    menu.handlers_menu(dp)
    text.handlers_text(dp)
    executor.start_polling(dp) 
    

