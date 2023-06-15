from create_bot import dp, bot
from aiogram import types, Dispatcher
from keyboards.client_kb import kb_client
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from data_base.db_open import cur_1

#@dp.message_handler(commands=["help"])

# обработка команды /start (стартовая клавиатура клавиатура и вывод сообщения)
async def cmd_start(message: types.Message, state: FSMContext):
    answer=cur_1.execute('SELECT Ответ FROM  Categories WHERE Категория==?', (message.text,)).fetchone()
    await message.answer(answer[0], reply_markup = kb_client)

#ответы на другие команды
async def cmd_menu(message: types.Message, state: FSMContext ):
    answer=cur_1.execute('SELECT Ответ FROM  Categories WHERE Категория==?', (message.text,)).fetchone()
    if len(answer[0])<4096:
        await message.answer(answer[0])
    else:
        for x in range (0, len(answer[0]), 4096):
            await message.answer(answer[0][x:x+4096])

async def find_term(message: types.Message, state: FSMContext):
    answer=cur_1.execute('SELECT Ответ FROM  Categories WHERE Категория==?', (message.text,)).fetchone()
    await message.reply(answer[0])

    

def handlers_menu (dp:Dispatcher):
    dp.register_message_handler(cmd_start, commands = ["start"], state = None)
    dp.register_message_handler(cmd_menu, commands = ["handbook", "help", "glossary"], state = None)
    dp.register_message_handler(find_term, commands = ["attack", "databasec", "informationsecurity", "malware",
                             "informationsystem", "information", "threatsource", "virus", "confidentiality",
                             "attacker", "unauthorizedaccess", "potential", "event", "threat",
                             "securitythreat", "vulnerability", "integrity", "authorization",
                             "authentication", "database", "botnet", "malprogramterm", "compnetwork",
                             "availabilityterm", "identification", "informationsystem", "confidentialityterm",
                            "cryptography", "nonrepudiation", "bufferoferflow", "securitypolicy","rootkit",
                             "worm", "socialengeneeringterm", "troy", "threatterm", "vulnerabilityterm",
                              "integrityterm","exploit", "Dos", "sqlinjection" ], state = None)
