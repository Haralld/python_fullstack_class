line = input("Введите строку: ")
words = line.split()

new_line = []

for word in words:
    new_line.append(word[::-1])

print(" ".join(new_line))

"""
Задача 1: Переверни слова

Описание:

Дана строка со словами. Напишите программу, которая переворачивает каждое слово в строке.


"""