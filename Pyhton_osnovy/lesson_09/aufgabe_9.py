 # Задача 1: Категория возраста
"""
Напишите метод define_age_category(age), который принимает возраст пользователя.
Метод должен вернуть:
- "Ребёнок", если возраст меньше 12.
- "Подросток", если возраст от 12 до 17.
- "Взрослый", если возраст от 18 и старше.
"""
"""
def define_age_category(age):
            if age < 12 :
                return "Ребенок"
            elif 12 <= age <=17:
                return"Подросток"
            else:
                return "Взрослый"
print(define_age_category(-21))
"""
# Задача 2: Допустимость для голосования
"""
Напишите метод can_vote(age), который принимает возраст пользователя.
Метод должен вернуть True, если возраст 18 или больше.
Иначе метод должен вернуть False.
"""
"""
def can_vote(age):
    if int(age) >= 18:
        return True
    else:
        return False

ageUser = input()
(can_vote (ageUser))

# Задача 3: Стоимость билетов

Напишите метод ticket_price(age), который принимает возраст.
Метод должен вернуть:
- Бесплатно, если возраст меньше 5.
- 10 долларов, если возраст от 5 до 18.
- 15 долларов, если возраст больше 18.
"""
def ticket_price(age):
    if age < 5:
        return "Бесплатно"
    elif 5 <= age < 18:
        return "10 долларов"
    else:
        return "15 долларов"
print(ticket_price(21))


