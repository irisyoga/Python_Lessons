
# Задание 1: Преобразование температуры
"""
Создайте метод celsius_to_fahrenheit(celsius), который принимает температуру в градусах Цельсия.
Метод должен преобразовать её в градусы Фаренгейта по формуле: F = C * 9/5 + 32.
Метод должен вернуть результат.
"""

def celsius_to_fahrenheit(temper):
    F = temper * 9 / 5 + 32
    #print(f"{F}") лишний принт
    return F

#celsius_to_fahrenheit(3) лишняя строка
mein_temper = celsius_to_fahrenheit(30)
print(f"{mein_temper}")

# Задание 2: Соединение слов
"""
Создайте метод join_words(word1, word2), который принимает два слова в виде строк.
Метод должен вернуть строку, где два слова объединены через пробел.
Пример: для слов "Привет" и "мир" метод должен вернуть "Привет мир".
"""

def join_words(word1, word2):
    words = [word1, word2]
    unionWords = " ".join(words)
    return unionWords

print(join_words("Привет", "мир"))

# Задание 3: Удаление пробелов
"""
Создайте метод remove_spaces(string), который принимает строку.
Метод должен вернуть эту строку, где удалены все пробелы.
Пример: для строки "Привет, мир!" метод должен вернуть "Привет,мир!".
"""

def remove_spaces(string):
    stringSecond = string.replace(" ","")
    return stringSecond

result = remove_spaces("Привет, мир!")

print(result)

# Задание 4: Замена символов
"""
Создайте метод replace_symbol(string, old, new), который принимает строку и два символа.
Метод должен заменить все вхождения символа old в строке на символ new и вернуть новую строку.
Пример: для строки "яблоко", old="о", new="а" метод должен вернуть "яблака".
"""

def replace_symbol(string, old, new):
    stringSecond = string.replace(old, new)
    return stringSecond

result = replace_symbol("яблоко",old="о", new="а")
print(result)

# Задание 5:
#Форматирование имени
"""
Создайте метод format_name(first_name, last_name), который принимает имя и фамилию.
Метод должен вернуть строку, где имя и фамилия записаны через пробел с заглавной буквы.
Пример: для "ильяс" и "иванов" метод должен вернуть "Ильяс Иванов".
"""
def format_name(first_name, last_name):
    string = first_name.capitalize()
    stringFirst = first_name.capitalize()
    stringSecond = last_name.capitalize()
    text = f"{stringFirst} {stringSecond}"
    return text

result = format_name("Iryna", "Haber")
print(result)


"""Полезные методы для работы со строками
Метод   Описание   Пример
.lower()    Преобразует строку в нижний регистр    "PYTHON".lower() -> "python"
.upper()    Преобразует строку в верхний регистр   "python".upper() -> "PYTHON"
.capitalize()   Делает первую букву строки заглавной   "python".capitalize() -> "Python"
.strip()    Удаляет пробелы в начале и конце строки    " hello ".strip() -> "hello"
.replace(a, b)  Заменяет подстроку a на b  "hello world".replace("world", "Python") -> "hello Python"
.split()    Разбивает строку на список по разделителю  "a,b,c".split(",") -> ["a", "b", "c"]
.join() Соединяет список строк с указанным разделителем    ",".join(["a", "b", "c"]) -> "a,b,c"
"""

