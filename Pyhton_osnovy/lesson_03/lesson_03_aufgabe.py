
text = "qwertyuio"
first_variable = text[0]
second_variable = text[1:]

first_variable = first_variable.upper()
result = first_variable + second_variable

print(result)

"""
name = "мир"
greeting = "Hello, " + name + "!"
print(greeting * 3)  # Output: Hello, Ilyas!
"""
#print(word[2])
#print(word[5])

startIndex = 4
endIndex = 6

file = "code.py"
print(file[4:6]) # подобная конструкция называется "срез" или подстрока
# Что это такое? Это часть строки начиная с символа, находящегося под индексом startIndex
# и заканчивая индексом endIndex, но не включая символ под индексом endIndex

# поэтому, если мы хотим увидеть строку, начиная от какого-то индекса, до конца, то мы можем использовать следующее:
print(file[startIndex:])

# Примеры применения полезных методов для работы со строками

# .lower() — Преобразует строку в нижний регистр
text = "PYTHON IS GREAT"
lower_case_text = text.lower()
print(lower_case_text)  # Вывод: python is great

# .capitalize() — Делает первую букву строки заглавной
text = "python is great"
capitalized_text = text.capitalize()
print(capitalized_text)  # Вывод: Python is great

# .strip() — Удаляет пробелы в начале и конце строки
text = "   Hello, Python!   "
stripped_text = text.strip()
print(stripped_text)  # Вывод: Hello, Python!

# .replace(a, b) — Заменяет подстроку `a` на `b`
text = "I love Java"
replaced_text = text.replace("Java", "Python")
print(replaced_text)  # Вывод: I love Python

# Пример с множественными заменами
text = "apples, oranges, apples"
replaced_text = text.replace("apples", "bananas")
print(replaced_text)  # Вывод: bananas, oranges, bananas

# .split() — Разбивает строку на части по разделителю
text = "apple,banana,orange"
fruit1 = text.split(",")[0]  # Первая часть
fruit2 = text.split(",")[1]  # Вторая часть
fruit3 = text.split(",")[2]  # Третья часть
print(fruit1)  # Вывод: apple
print(fruit2)  # Вывод: banana
print(fruit3)  # Вывод: orange

# Пример с разделением по пробелам
text = "Learn Python Programming"
word1 = text.split()[0]  # Первое слово
word2 = text.split()[1]  # Второе слово
word3 = text.split()[2]  # Третье слово
print(word1)  # Вывод: Learn
print(word2)  # Вывод: Python
print(word3)  # Вывод: Programming

# .join() — Соединяет части строки с указанным разделителем
fruit1 = "apple"
fruit2 = "banana"
fruit3 = "orange"
joined_fruits = fruit1 + ", " + fruit2 + ", " + fruit3
print(joined_fruits)  # Вывод: apple, banana, orange

# Пример с соединением слов через дефис
word1 = "Learn"
word2 = "Python"
word3 = "Programming"
joined_words = word1 + "-" + word2 + "-" + word3
print(joined_words)  # Вывод: Learn-Python-Programming