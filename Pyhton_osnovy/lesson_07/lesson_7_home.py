

#Метод, который вычисляет площадь круга по заданному радиусу и возвращает площадь круга.
# Исходные данные 1:
def calculate_circle_area(radius):
    pi = 3.14
    circle_area = pi * (radius ** 2)   #Радиус круга (float или int)
    return circle_area                 #Площадь круга (float)

# Пример использования:
radius = float(input("Введите радиус круга:"))
area = calculate_circle_area(radius)
# Вывод результата:
print(f"Площадь круга с радиусом {radius} = {area:.2f}")

#Метод, который объединяет имя и фамилию и возвращает в виде аргумента в одну строку.
# Исходные данные 2:
def concat_names(firstName, lastName):
    return f"{firstName} {lastName}"
# Пример использования:
firstName = input("Введите имя:")
lastName = input("Введите фамилию:")
fullName = concat_names(firstName, lastName)
# Вывод результата:
print(f"Полное имя: {fullName}")

#Метод, который принимает имя пользователя и сообщение в качестве аргументов и возвращает форматированное сообщение:
# Исходные данные 3:
def format_message(userName, message):
    return f"[{userName}]: [{message}]"
# Пример использования:
userName = input("Введите имя пользователя:")
message = input("Введите сообщение:")
formatMessage = format_message(userName, message)
# Вывод результата:
print(f"Форматированное сообщение: {formatMessage}")

#Метод, который принимает слово и число в качестве аргументов
# и возвращает строку, где слово без пробелов, например:"Привет" повторяется 3 раза.
# Исходные данные 4:
def duplicate_word(word, count):
    return word * count
# Пример использования:
word = input("Введите слово:")
count = int(input("Введите количество повторений:"))
result = duplicate_word(word, count)
# Вывод результата:
print(f"Строка повторится {count} раза: {result} ")










