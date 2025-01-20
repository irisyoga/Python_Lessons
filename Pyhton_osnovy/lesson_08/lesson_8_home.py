
#Сравнение температур:
#Напишите метод is_warmer_than, который принимает два аргумента: две температуры.
#Метод должен возвращать True, если первая температура выше второй.
#Иначе метод должен возвращать False.

#Метод, который сравнивает две температуры.
# Исходные данные 1:

def is_warmer_than(temp1, temp2):
    if temp1 > temp2:
        return True
    else:
        return False

# Пример использования:
temp1 = float(input("Введите первую температуру:"))
temp2 = float(input("Введите вторую температуру:"))
# Вывод результата:
if is_warmer_than(temp1, temp2):
   print(f"Температура {temp1}  выше, чем {temp2}.")
else:
    print(f"Температура {temp1} не выше, чем {temp2}.")

#Проверка порядка строк:
#Напишите метод is_substring_first, который принимает две строки.
#Метод должен возвращать True, если первая строка находится раньше второй в алфавитном порядке.
#Иначе метод должен возвращать False.

# Исходные данные 2:
def is_substring_first(str1, str2):
    if str1 < str2:
        return True
    else:
        return False
# Пример использования:
str1 = input("Введите первую сроку:")
str2 = input("Введите вторую сроку:")
# Вывод результата:
if is_substring_first(str1, str2):
    print(f"Строка '{str1}' находиться раньше строки '{str2}' в алфавитном порядке.")
else:
    print(f"Строка '{str1}' не находиться раньше строки '{str2}' в алфавитном порядке.")


#Кратность числа:
#Напишите метод is_multiple_of, который принимает два числа.
#Метод должен возвращать True, если первое число кратно второму.
#Иначе метод должен возвращать False.

# Исходные данные 3:
def is_multiple_of(number, divisor):
    if divisor == 0:
       return ValueError        #Делитель не может быть равен нулю
    elif number % divisor == 0: # Проверяем, является ли первое число кратным второму
        return True
    else:
        return False

# Пример использования:
number = int(input(f"Введите первое число:"))
divisor = int(input(f"Введите второе число:"))

# Вывод результата:
if divisor == 0:
    print("Ошибка, делитель не может быть равен нулю:")
if is_multiple_of(number, divisor):
    print(f"число {number} кратно числу {divisor}.")
else:
    print(f"число {number} не кратно числу {divisor}.")

#Сравнение длины строк:
#Напишите метод is_longer_than, который принимает две строки.
#Метод должен возвращать True, если первая строка длиннее второй.
#Иначе метод должен возвращать False.

# Исходные данные 4:
def is_longer_than(str1, str2):
    if len(str1) > len(str2):
        return True
    else:
        return False

# Пример использования:
str1 = input("Введите первую строку:")
str2 = input("Введите вторую строку:")

# Вывод результата:
if is_longer_than(str1, str2):
    print(f"Первая строка длиннее второй.")
else:
    print(f"Первая строка не длиннее второй.")

#Строка содержит цифру:
#Напишите метод contains_digit, который принимает строку.
#Метод должен возвращать True, если строка содержит хотя бы одну цифру.
#Иначе метод должен возвращать False.

# Исходные данные 5:
def contains_digit(string):
   if (
        "0" in string or
        "1" in string or
        "2" in string or
        "3" in string or
        "4" in string or
        "5" in string or
        "6" in string or
        "7" in string or
        "8" in string or
        "9" in string ):
        return True
   else:
        return False
# Пример использования:
string = input("Введите строку:")

# Вывод результата:
if contains_digit(string):
    print("Строка содержит хотя бы одну цифру.")
else:
    print("Строка не содержит цифр.")

