# Задача: предложить улучшения кода для четырёх уже решённых задач из семинаров №№ 2 - 5
# с помощью использования лямбд, filter, map, zip, enumerate, list comprehension
# - В решении указывайте как старый вариант (до улучшения), так и новый.
# - Обязательно, комментариями в коде, указывайте условие задачи.

# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

file = open('file.txt', 'r')
text = file.read()
file.close()

text_array = text.split()

print("old: ", text)
# new_text_array = []
# for i in range(0, len(text_array)):
#     if text_array[i].find("абв") < 0:
#         new_text_array.append(text_array[i])

new_text_array = list(filter(lambda i: i.find("абв") < 0, text_array)) # Использовал Filter и Lambda


new = str(new_text_array[0])
for i in range(1, len(new_text_array)):
    new = new + " " + str(new_text_array[i])

print("new: ", new)