
#Исходные данные: конфета стоит 3 у.е., у Вас есть 27 у.е.
# Напишите программу, которая сохраняет эти данные в переменных,
# вычисляет и выводит в консоль, сколько конфет Вы можете купить.
#Исходные данные 1:
price_candy_1 = 3 #Цена одной конфеты
total_money = 27  #Общая сумма денег
#Вычисление количества конфет:
candies_count = total_money//price_candy_1
#Вывод результата:
print("Вы можете купить -", candies_count ,"конфет")

#Исходные данные: конфета стоит 3 у.е., мороженое стоит 5 у.е.
# Вы хотите купить 7 конфет и 3 мороженых. Напишите программу,
# которая сохраняет эти данные в переменных, вычисляет и выводит в консоль,
# сколько денег Вам потребуется.
#Исходные данные 2:
price_candy_1 = 3 #Цена одной конфеты
price_icecream_1 = 5 #Цена одного мороженого
wanted_candies = 7   #Количество конфет, которые хотите купить
wanted_icecream = 3  #Количество морожденого, которое хотите купить
#Вычисление общей стоимости:
total_cost = (wanted_candies * price_candy_1) + (wanted_icecream * price_icecream_1)
#Вывод результата:
print("Вам потребуется -", total_cost , "euro")



