from create_bot import dp, bot
from aiogram import types, Dispatcher
from data_base.db_open import cur, cur_1
from keyboards.client_kb import kb_client, kb_base
from fuzzywuzzy import fuzz, process
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

#состояние поиска в базе уязвимостей
class states(StatesGroup):
    vulbase = State()

#при вводе команды /vulbase переходим в режим поиска в базе уязвимостей
async def base_start(message:types.Message, state: FSMContext):
    answer=cur_1.execute('SELECT Ответ FROM  Categories WHERE Категория==?', (message.text,)).fetchone()
    await message.reply(answer[0], reply_markup = kb_base)
    await states.vulbase.set() 

# по команде /cancel выходим из режима
async def base_end(message:types.Message, state: FSMContext):
    answer=cur_1.execute('SELECT Ответ FROM  Categories WHERE Категория==?', (message.text,)).fetchone()
    await message.reply(answer[0],reply_markup = kb_client)
    await state.set_state(state = None)

# в режиме поиска в базе ищем ответ на основе точного названия или нечеткого сравнения
async def cmd_text(message: types.Message, state: FSMContext):
    if message.text[0] != '/':
        r=cur.execute('SELECT * FROM threats WHERE №==?', (message.text,)).fetchone()
        if (r!=None):
             await message.answer(f'<b>№</b>:{r[0]}\n<b>Название</b>:{r[1]}\n<b>Тип активов</b>:{r[2]}\n<b>Конфиденциальность</b>:{r[3]}\n<b>Целостность</b>:{r[4]}\n<b>Доступность</b>:{r[5]}\n<b>Потенциал внешнего нарушителя</b>:{r[6]}\n<b>Потенциал внутреннего нарушителя</b>:{r[7]}\n<b>Описание</b>:{r[8]}\n', parse_mode="HTML")
        else:
            mas = cur.execute("Select Название from threats ").fetchall()
            string = message.text
            max = 0 
            for x in mas:
                a = fuzz.partial_ratio(string, x)
                if a>max:
                    max = a
                    b = x
            if max >= 70:
                r = cur.execute("Select * From threats where Название==?", (b)).fetchone()
                await message.answer(f'<b>№</b>:{r[0]}\n<b>Название</b>:{r[1]}\n<b>Тип активов</b>:{r[2]}\n<b>Конфиденциальность</b>:{r[3]}\n<b>Целостность</b>:{r[4]}\n<b>Доступность</b>:{r[5]}\n<b>Потенциал внешнего нарушителя</b>:{r[6]}\n<b>Потенциал внутреннего нарушителя</b>:{r[7]}\n<b>Описание</b>:{r[8]}\n', parse_mode="HTML")
            else:
               r = '/error'
               answer=cur_1.execute('SELECT Ответ FROM  Categories WHERE Категория==?', (r, )).fetchone()
               await message.answer(answer[0])

# в обычном режиме отвечаем пользователю на основе обученной модели
async def cmd_text_2(message: types.Message, state: FSMContext):
        if message.text[0] != '/':
            import pickle
            from ML.preprocessing import text_preprocessing
            import pandas as pd
            text = text_preprocessing(message.text)
            print(text)
            x=[text]
            with open ('data.pickle', 'rb') as f:
                text_clf = pickle.load(f)
            pre = text_clf.predict(x)
            scores = text_clf.predict_proba(x).tolist()[0]
            print(scores)
            print(pre[0])
            if max(scores)<0.3:
                print(message.text)
                f = open('dataset.txt', 'r')
                maximum = 0 
                for line in f:
                    if pre[0] in line:
                        print(line)
                        a = fuzz.partial_ratio(message.text, line)
                        if a>maximum: maximum=a
                print(maximum)
                if maximum<70:
                   pre[0] = '/error'
            answer=cur_1.execute('SELECT Ответ FROM  Categories WHERE Категория==?', (pre[0], )).fetchone()
            await message.reply(answer[0])

def handlers_text (dp:Dispatcher):
    dp.register_message_handler(base_start, commands=["vulbase"], state = None)
    dp.register_message_handler(base_end, commands=["cancel"], state = states.vulbase)
    dp.register_message_handler(cmd_text, state = states.vulbase)
    dp.register_message_handler(cmd_text_2, state = None )
