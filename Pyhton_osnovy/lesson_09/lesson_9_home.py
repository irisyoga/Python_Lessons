
#Диапазон температуры:
#Напишите метод is_in_temperature_range, который принимает температуру и
# два предела (min и max) в качестве аргументов.
#Метод должен возвращать True, если температура находится в диапазоне [min, max].
#Иначе метод должен возвращать False.

# Исходные данные 1:
def is_in_temperature_range(temp, min_temp, max_temp):
    if  min_temp <= temp <= max_temp:
        return True
    else:
        return False

# Пример использования:
temp = float(input("Введите  температуру:"))
min_temp = float(input("Введите минимальную границу диапазона температуры:"))
max_temp = float(input("Введите максимальную границу диапазона температуры:"))

# Вывод результата:
if is_in_temperature_range(temp, min_temp, max_temp):
      print(f"Температура находится в пределах диапазона: {is_in_temperature_range(temp, min_temp, max_temp)}")
else:
      print(f"Температура не находится в пределах диапазона: {is_in_temperature_range(temp, min_temp, max_temp)}")

#Алфавитное сравнение:
#Напишите метод compare_alphabetical_order, который принимает два слова.
#Метод должен возвращать "Первое", если первое слово идёт раньше в алфавите, "Второе",
# если второе идёт раньше, или "Равно", если слова одинаковые.

# Исходные данные 2:
def compare_alphabetical_order(word1, word2):
    if word1 < word2:
        return "Первое"
    elif word1 > word2:
        return "Второе"
    else:
        return "Равно"
# Пример использования:
word1 = input("Введите первое слово:")
word2 = input("Введите второе слово:")
# Вывод результата:
print(compare_alphabetical_order(word1, word2))

#Проверка чётности и положительности:
#Напишите метод is_even_and_positive, который принимает число.
#Метод должен возвращать True, если число чётное и положительное.
#Иначе метод должен возвращать False.

# Исходные данные 3:
def is_even_and_positive(number):
    if number > 0 and number % 2 == 0:
        return True
    else:
        return False

# Пример использования:
number = int(input(f"Введите число:"))
if is_even_and_positive(number):
    print ("True")
else:
    print("False")

#Проверка возрастной группы:
#Напишите метод get_age_group, который принимает возраст.
#Метод должен возвращать:
#"Младенец", если возраст меньше 3.
#"Ребёнок", если возраст от 3 до 12.
#"Подросток", если возраст от 13 до 19.
#"Взрослый", если возраст 20 и старше.

# Исходные данные 4:
def get_age_group (age):
    if age < 3:
        return "Младенец"
    elif 3 <= age <= 12:
        return "Ребенок"
    elif 13 <= age <= 19:
        return "Подросток"
    else:
        return "Взрослый"
# Пример использования:
age = int(input(f"Введите возраст:"))
# Вывод результата:
print(f"Возрастная группа: {get_age_group(age)}")

#Проверка надёжности пароля:
#Напишите метод is_strong_password, который принимает строку пароля.
#Метод должен возвращать True, если пароль содержит не менее 8 символов и включает как буквы, так и цифры.
#Иначе метод должен возвращать False.

# Исходные данные 5:
# r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
import re
def is_strong_password(password):
    pattern = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
    if bool(re.match(pattern, password)):
        return True
    else:
        return False

# Пример использования:
user_password = input("Введите ваш пароль:")

#Проверяем пароль и выводим результат:
if is_strong_password(user_password):
    print("Пароль надежный.")
else:
    print("Пароль не надежный. Он должен содержать минимум 8 символов, включая буквы и цифры")

#Определение сезона:
#Напишите метод get_season, который принимает номер месяца (1 для января, 12 для декабря).
#Метод должен возвращать сезон ("Зима", "Весна", "Лето", "Осень") в зависимости от месяца.

# Исходные данные 6:
def get_season(month):
    if 3 <= month <= 5:
        return "Весна"
    if 6 <= month <= 8:
        return "Лето"
    if 9 <= month <= 11:
        return "Осень"
    else:
        return "Зима"
# Пример использования:
month = int(input("Введите номер месяца(1-12):"))
season = get_season(month)
# Вывод результата:
print(f"Сезон: {season}")

#Проверка длины строки:
#Напишите метод is_valid_length, который принимает строку и максимальную длину.
#Метод должен возвращать True, если длина строки меньше или равна максимальной длине.
#Иначе метод должен возвращать False.

# Исходные данные 7:

def is_valid_length(string, maxLen):
    if len(string) <= maxLen:
        return True
    else:
        return False

# Пример использования:
maxLen = int(input(f"Введите максимальное значение длины:"))
string = input("Введите строку:")

if is_valid_length(string, maxLen):
    print("Длина строки допустима")
else:
    print("Длина строки не допустима")
#Проверяем строку и выводим результат:
print(f"Строка: {string} длиной: {len(string)}.")

#Тип треугольника:
#Напишите метод get_triangle_type, который принимает три стороны треугольника.
#Метод должен возвращать:
#"Равносторонний", если все стороны равны.
#"Равнобедренный", если две стороны равны.
#"Разносторонний", если все стороны разные.

# Исходные данные 8:

def get_triangle_type(a, b, c):
    if a == b == c:
        return "Равносторонний"
    elif a == b or b == c or a == c:
        return "Равнобедренный"
    else:
        return "Разносторонний"

# Пример использования:
a = input("Введите длину первой стороны:")
b = input("Введите длину второй стороны:")
c = input("Введите длину третей стороны:")

triangle_type = get_triangle_type(a, b, c)
# Вывод результата:
print(f"Тип треугольника:{triangle_type}")
