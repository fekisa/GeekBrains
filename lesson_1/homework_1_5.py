#5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

proceeds = int(input("Введиту сумму выручки: "))
costs = int(input("Введиту сумму издержек: "))
result = proceeds-costs

if proceeds > costs:
    efficiency = result/proceeds
    print(f'''Ваша прибыль составила:{result}.
Рентабельность: {efficiency}''')
    employee = int(input("Введите количество сотрудников: "))
    income_per_person = result / employee
    print(f"Прибыль в расчете на одного сотрудника составляет:{income_per_person}")
elif proceeds == costs:
    print("Вы отработали в 0")
else:
    print(f"Ваш убыток составил: {result}")

# проверка данных if proceeds.isdigit:  , но более правильно использовать try : except