import itertools
import sqlite3

categories_tasks = [
    {'title': '/help', 'options': [
     'себе', 'функционал']},
     {'title': '/attack', 'options': [
     'атака', 'компьютерная атака']},
    {'title': '/database', 'options': [
        'база данных', 'бд']},
    {'title': '/informationsecurity', 'options': ['безопасность информации', 'безопасность']},
    {'title': '/malware', 'options': [
        'малварь', 'вредоносная программа']},
    {'title': '/virus', 'options': [
        'компьютерный вирус', 'вирус']},
    {'title': '/vulnerability', 'options': [
        'уязвимость', 'уязвимость информационной безопасности']},
    {'title' : '/availability', 'options': [
        'доступность', 'доступность информации']},
    {'title': '/informationsystem', 'options':[
        'информационная система', 'ис']},
    {'title': '/information', 'options':[
        'информация']},
    {'title': '/threatsource', 'options': [
        'источник угрозы безопасности', 'источник угрозы']},
    {'title': '/confidentiality', 'options':[
        'конфиденциальность', 'конфиденциальность информации']},
    {'title': '/attacker', 'options':[
        'нарушитель безопасности', 'атакующий']},
    {'title': '/unauthorizedaccess', 'options':[
     'несанкционированный доступ']},
    {'title': '/potential', 'options':[
      'потенциал нарушителя', 'потенциал']},
    {'title': '/event', 'options':[
       'событие информационной системы', 'событие']},
    {'title': '/threat', 'options':[
        'угроза']},
    {'title': '/securitythreat', 'options':[
        'угроза информационной безопасности']},
    {'title': '/integrity', 'options':[
        'целостность информации', 'целостность']},
    {'title': '/glossary', 'options':[
        'глоссарий', 'словарь', 'термины']
        }
]


prepositions = ['о', 'про', '']
extra_words = ['рассказать', 'узнать', ' ' ]
with open("dataset.txt", 'a') as f:
    for category in categories_tasks:
        for tup in itertools.product(
            extra_words,
            prepositions, category['options']):
         sample = ' '.join(tup)
         term = category["title"] + ' '
         f.write(f'{sample}@{category["title"]}\n')
