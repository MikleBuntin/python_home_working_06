# Задача: предложить улучшения кода для четырёх уже решённых задач из семинаров №№ 2 - 5
# с помощью использования лямбд, filter, map, zip, enumerate, list comprehension
# - В решении указывайте как старый вариант (до улучшения), так и новый.
# - Обязательно, комментариями в коде, указывайте условие задачи.

# Задание 2.
# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial(n):
    factorial = 1
    for number in range(1, n + 1):
        factorial = factorial * number
    return factorial

n = int(input("Введите целое положительное число: "))

# array = []
# for count in range(n):
#     array.append(factorial(count))

array = [factorial(count) for count in range(n)] # Использовал List comprehensions

print(array)