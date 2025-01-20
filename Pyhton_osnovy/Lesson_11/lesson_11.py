
# представим, что у нас есть 10 растений,
# каждое из которых надо полить:

# старый код:

print("старый формат:")
print("Поливаю растение 1")
print("Поливаю растение 2")
print("Поливаю растение 3")
print("Поливаю растение 4")
print("Поливаю растение 5")
print("...")
print("Поливаю растение 10")

print("\nновый формат:")

counter = 10

while counter > 0:
    print(f"Поливаю растение номер {11 - counter}")
    counter = counter - 1

print("Закончил поливать растения.")

print("Привет! Придумайте пожалуйста пароль для нашего сервиса\n")

password = input()

while len(password.strip()) < 10:
    print(f"Длина пароля не достаточна. Ваш пароль {password.strip()} содержит только {len(password.strip())} символов. "
          f"Введите новый пароль:\n")
    password = input()

    print("Привет! Придумайте пожалуйста пароль для нашего сервиса:\n")

    password = input()

    while len(password.strip()) < 10:
        print(
            f"Длина пароля не достаточна. Ваш пароль {password.strip()} содержит только {len(password.strip())} символов. \n "
            f"Если вы хотите закончить работу, то введите 0\n"
            f"Введите новый пароль:\n")
        password = input()
        if password == "0":
            print("Так как вы ввели 0, пароль не был установлен")
            break

            sum = 0
            num = int(input("enter your number:"))

            while True:

                if num % 2 == 0:
                    print("введено четное число, пропускаем суммирование")
                    num = int(input("enter your number:"))
                    continue

                sum = sum + num

                if sum > 100:
                    print("сумма больше 100б останавливаем работу цикла")
                    break

                num = int(input("enter your number:"))

            print(sum)

