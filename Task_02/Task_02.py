# Задача: предложить улучшения кода для четырёх уже решённых задач из семинаров №№ 2 - 5
# с помощью использования лямбд, filter, map, zip, enumerate, list comprehension
# - В решении указывайте как старый вариант (до улучшения), так и новый.
# - Обязательно, комментариями в коде, указывайте условие задачи.

# Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.
# *Пример*
# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]

import random
original_array = []
count = int(input("Введите количество элементов исходного массива: "))

# for i in range(1, count):
#     original_array.append(random.randint(0, 4))

original_array = [random.randint(0, 4) for i in range(0, count)] # использовал List Comprehensions

array = []
array.append(original_array[0])
for number in original_array:
    if number not in array:
        array.append(number)

print(original_array)
print(array)
