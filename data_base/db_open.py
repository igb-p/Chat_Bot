import sqlite3 as sq
from create_bot import bot


def sql_start():
    global data, cur
    # база данных для обучения
    data=sq.connect('threats.db')
    cur=data.cursor()

    #база данных для ответов
    global data_1, cur_1
    data_1 = sq.connect('Категории.db')
    cur_1 = data_1.cursor()
