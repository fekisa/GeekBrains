'''Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
'''

user_list = [
    "строка",
    5,
    ["список", 2],
    (1, 2),
    {'ключ': 'значение'},
]
print(list)

#вариант 1
for i in user_list:
    print(type(i))

#вариант 1
for i in user_list:
    print(f'{i} - {type(i)}')