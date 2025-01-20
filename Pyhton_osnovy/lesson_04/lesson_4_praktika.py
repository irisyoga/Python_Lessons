
# Задание 1: Преобразование регистра
"""
Создайте строку с текстом "Python Programming IS Awesome!".
Выполните следующие операции:
- Преобразуйте строку в нижний регистр.
- Преобразуйте строку в верхний регистр.
- Сделайте первую букву строки заглавной.
"""
text = "Programming IS Awesome!"
print(text)
lower_text = text.lower()             # .lower() — Преобразует строку в нижний регистр
print(lower_text)
upper_text = text.upper()             # .upper() — Преобразует строку в верхний регистр
print(upper_text)
capitalized_text = text.capitalize()  # .capitalize() — Делает первую букву строки заглавной
print(capitalized_text)
# Задание 2: Удаление лишних пробелов
"""
Создайте строку с текстом "   Привет, Python!   ".
- Удалите пробелы в начале и конце строки.
- Выведите результат.
"""
text = "      Привет, Python!      "
print(text)
stripped_text = text.strip()          # .strip() — Удаляет пробелы в начале и конце строки
print(stripped_text)
# Задание 3: Замена подстроки
"""
Создайте строку с текстом "Я изучаю Java".
- Замените слово "Java" на "Python".
- Выведите результат.
"""
text = "Я изучаю Java"
print(text)
replaced_text = text.replace("Java", "Python")  # .replace(a, b) — Заменяет подстроку `a` на `b`
print(replaced_text)
# Задание 4: Разделение строки
"""
Создайте строку с текстом "яблоко,банан,вишня".
- Разбейте её на отдельные слова, используя запятую как разделитель.
- Выведите полученный список.
"""
text = "яблоко,банан,вишня"
print(text)
fruit1 = text.split(",")[0]      # .split() — Разбивает строку на части по разделителю
fruit2 = text.split(",")[1]
fruit3 = text.split(",")[2]
print(fruit1)
print(fruit2)
print(fruit3)
# Задание 5: Объединение строки
"""
Создайте список: ["Привет", "мир", "Python"].
- Соедините элементы списка в одну строку, используя пробел в качестве разделителя.
- Выведите результат.
"""
words_list = ["Привет", "мир", "Python"]                 #список
print(words_list)

joined_words = " " .join (["Привет", "мир", "Python"])  #элементы списка в одну строку, используя пробел                                                        # в качестве разделителя
print(joined_words)
# Задание 6: Комбинированное использование методов
"""
Создайте строку с текстом "  Hello, PYTHON WORLD!  ".
- Удалите пробелы в начале и конце строки.
- Преобразуйте строку в нижний регистр.
- Замените слово "python" на "Java".
"""
text = "  Hello, PYTHON WORLD!   "
print(text)
text = text.strip()
print(text)
text = text.lower()
print(text)
text = text.replace("python","java")
print(text)
# Задание 7: Работа со списком слов
"""
Создайте строку с текстом "учеба, кодинг, отдых, прогулка".
- Разбейте строку на слова.
- Сделайте каждое слово заглавным (с большой буквы).
- Объедините слова обратно в строку, разделяя их запятыми.
"""
# Исходная строка
text = "учеба, кодинг, отдых, прогулка"
# Разбиваем строку на список слов
words = text.split(", ")
print(words)
# Делаем каждое слово заглавным (с большой буквы)
capitalized_words = [word.capitalize() for word in words]
print(capitalized_words)
# Объединяем слова обратно в строку с разделителем запятая
result = ", ".join(capitalized_words)
# Выводим результат
print(result)

# Задание 8: Частотный анализ
"""
Создайте строку с текстом "Python Python Python Java Java C++".
- Разбейте строку на отдельные слова.
- Подсчитайте, сколько раз каждое слово встречается в строке.
- Выведите результаты.
"""
text = "Python Python Python Java Java C++"
words_tuple = text.split()                         # .split() — Разбивает строку на части по разделителю
print(words_tuple)

print(words_tuple.count("Python"))
print(words_tuple.count("Java"))
print(words_tuple.count("C++"))

