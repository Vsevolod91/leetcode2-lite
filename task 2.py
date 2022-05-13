# Задача 2
# Пользователь в цикле вводит 10 производных цифр. Выведите количество введеных пользователем цифр 5.

number_str = 0
sum_len = 0

while number_str < 10:
    number_str += 1
    print(number_str, "число")
    sum_len = sum_len + len(input("Введите любое число: "))
print(sum_len)