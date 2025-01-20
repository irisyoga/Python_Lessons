"""
name = "Iryna"
day = 9
print(f"Hi, {name} today is {day}")
print(f"Hi, {name} today is {day:>3}")       #Hi, Iryna today is   9
print(f"Hi, {name} today is {day:0>3}")      #Hi, Iryna today is 009
print(f"Hi, {name} today is {day:0<3}")      #Hi, Iryna today is 900
print(f"Hi, {name} today is {day:0^3}")      #Hi, Iryna today is 090
print(f"Hi, {name:_^10} today is {day:0^3}") #Hi, __Iryna___ today is 090

month = 1
year = 2025
print(f"{day:0>2}.{month:0>2}.{year}") #09.01.2025
#age = int(age)
#age = input("Enter you age: ") #Enter you age: 21

array = "apple banana orange".split(" ")
print(array)
array = "apple banana orange".split()
print(array)
array = "apple\nbanana\norange".split("\n")
print(array)
array = "apple::banana::orange".split("::")
print(array)
data = "apple banana orange".split(" ")

for index,elem in enumerate(data):
    data[index] = f"{index + 1:0>2}.{elem}"
    print(f"{index + 1:0>2}.{elem}")


def print_hello():
    print("Hello world!")
    print("Bye world!")
print_hello()

def print_hello(name="John"):
    print(f"Hello, {name}!")

print_hello("John")
print_hello("Jane")
print_hello("Jim")
print_hello()
"""
"""
import random

def guess_number(start, end):
    rand_number = random.randint(start, end) # случайное число от 1 до 10
    user_number = int(input("Введите число от 1 до 10: "))

    if rand_number == user_number:
        print("Вы угадали число!")
    else:
        print(f"Вы не угадали число! Правильный ответ: {rand_number}")

def main():
    while True:
        guess_number()

        if input("Хотите сыграть еще раз? (y/n): ") == "n":
            break


if __name__ == "__main__":
    main()


if 2 + 2 == 5:
   print("2 + 2 = 5")
if 1 + 1 == 2:
        print("1 + 1 = 2")
elif 2 + 2 == 3:
  print("2 + 2 = 3")
elif 2 + 2 == 2:
    print("2 + 2 = 2")
elif 2 + 2 == 4:
    print("2 + 2 = 4")
else:
    print("2 + 2 != 5, 3, 2, 4")
i = 0
while i < 10:
    i += 1

    # if i % 2 == 0:
    #     continue
    if i == 5:
        break

    print(i)

print("Done")

# ----

for i in range(10):
    print(i)

print("Done")
"""
# Задача 4: разработать программу, которая умеет зашифровывать и
#   расшифровывать короткие текстовые сообщения методом шрифта Цезаря.
# Детали
# 1. Пользователь вводит сам текст (например, фразу).
# 2. Указывает, хочет он «зашифровать» или «расшифровать» (логический выбор).
# 3. Вводит число сдвига (целое, например, от 1 до 25).
# 4. Программа пробегается по каждой букве во введённом тексте и смещает её в алфавите на заданное количество позиций.
#     - Для «зашифровки» двигаем вперёд (A→C при сдвиге 2).
#     - Для «расшифровки», наоборот, двигаем в обратную сторону.
# 5. Программа игнорирует пробелы, цифры, знаки препинания или обрабатывает их особо — по вашему желанию.
# 6. Выводит результат в консоль (зашифрованную строку или расшифрованную).
# 7. Спрашивает, хочет ли пользователь повторить, и организует цикл (например, while) до тех пор, пока не будет введена команда выхода.

def caesar_cipher(data, mode, key):
    result = ''

    for symbol in data:
        symbol_number = ord(symbol)
        if mode == 1:  # расшифровать
            symbol_number = symbol_number - key
        else:  # зашифровать
            symbol_number = symbol_number + key

        new_symbol = chr(symbol_number)
        result += new_symbol

    return result


def main():
    while True:
        data = input("\nEnter message: ")
        mode = int(input("Enter mode (1. расшифровка, 2. зашифровка): "))
        key = int(input("Enter key: "))

        result = caesar_cipher(data, mode, key)

        print(f"Result: {result}")

        if input("\nПовторить? (y/n): ") == "n":
            break


if __name__ == "__main__":
    main()




# Задача 1: разработать игру крестики-нолики для одного игрока, в качестве второго игрока будет выступать сама программа.
# Детали:
# 1. Игровое поле представляет собой квадрат 3x3.
# 2. Игрок и программа ходят по очереди, ставя на свободные клетки поля свои символы (игрок - "X", программа - "O").
# 3. Программа должна иметь простую стратегию для выбора хода (например, случайный выбор).
# 4. Игра заканчивается, когда один из игроков выстраивает три своих символа в ряд по горизонтали,
# вертикали или диагонали, либо когда все клетки поля заняты (ничья).
# 5. После каждого хода необходимо отображать текущее состояние игрового поля.
# 6. В конце игры выводится результат: победа игрока, победа программы или ничья.
game_map = [
    [None, None, None],
    [None, "X", None],
    [None, None, "0"]
]
def game_map_user():
    x, y = input("Введите координаты: ").split()
    x = int(x)
    y = int(y)
    if not (0 <= x < 3 and 0 <= y < 3):
        return False
    if game_map[y][x] is not None:
        return False
    game_map[y][x] = "X"
    print(f"я сходил: {y} {x}")
    return True
def game_map_bot():
    pass



def main(): # Если game_map_user выдает True, то ход передается боту, иначе повторяем ход юзера.
    # Проверка игрового поля.
    pass

def game_map_dash():
    for i in range(3):
        for j in range(3):
            if game_map[i][j] is None:
                print("_", end = " ")
            else:
                print(game_map[i][j], end = " ")
        print("")

game_map_dash()


import random

def guess_number(start, end):
    rand_number = random.randint(start, end) # случайное число от 1 до 10
    user_number = int(input("Введите число от 1 до 10: "))

    if rand_number == user_number:
        print("Вы угадали число!")
    else:
        print(f"Вы не угадали число! Правильный ответ: {rand_number}")


def main():
    while True:
        guess_number()

        if input("Хотите сыграть еще раз? (y/n): ") == "n":
            break


if __name__ == "__main__":
    main()
