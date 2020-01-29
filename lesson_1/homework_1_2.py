#2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк. (% остаток от деления)

input_second = int(input('Введите количество секунд: '))

hour = (input_second // 3600) % 24
minute = (input_second // 60) % 60
second = input_second % 60

print(f"{hour}:{minute}:{second} ")

# другая запись решения
input_second = int(input('Введите количество секунд: '))
print(f"{input_second // 3600:02} - {input_second % 3600 // 60:02} - {input_second % 3600 % 60:02}")