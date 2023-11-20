word = "Design"
slogan = input("Введите описание: ")
number_of_occurrences = 0 

word_index = slogan.find(word)

while word_index != -1:
    number_of_occurrences += 1
    word_index = slogan.find(word, word_index + 1)


print(f"Колличество вхождений: {number_of_occurrences}")

"""
Задание 4: Подсчет частоты вхождений

Описание:

Роман интересуется, сколько раз слово "Design" теперь встречается в различных новых описаниях.


"""