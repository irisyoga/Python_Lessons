
"""
*** (Необязательное, сложное):
Напишите программу, которая сохраняет цену $123.456789 в переменной и выводит её:
Округлённой до 2 знаков после запятой.
В двоичной, восьмеричной и шестнадцатеричной системах счисления.
"""
# Исходные данные 6:
price = 123.456789                     #Сохраняем цену в переменной
roundedPrice = round(price, 2)         #Округляем до двух знаков после запятой
integerPrice = int(roundedPrice * 100) #Переводим в целое число (умножаем на 100
                                       #для точности до копеек)
# Преобразование в другие системы:
binaryPrice = bin(integerPrice)        #Двоичная система
octalPrice = oct(integerPrice)         #Восьмиричная система
hexadecimalPrice = hex(integerPrice)   #Шестнадцатиричная система

# Выводим результат:
print(f"Округленная цена: ${roundedPrice}")
print(f"В двоичной системе: {binaryPrice}")
print(f"В шестнадцатиричной системе: {hexadecimalPrice}")