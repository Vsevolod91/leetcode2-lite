# Задача 4
# Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран(можно поискать в интернете алгоритм факториала в python).

number = 0
mult_number = 1

while number < 10:
    number += 1
    mult_number = mult_number * number
print(mult_number)