
example = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

print("len(example) = ", len(example))
print(example[len(example) - 1])

print("example[0] = ", example[0])
print("example[5] = ", example[5])
print("example[0:5] = ", example[0:5])
print("example[1:5] = ", example[1:5])
print("example[5:] = ", example[5:])
print("example[:5] = ", example[:5])
print("example[-5:] = ", example[-5:])
print("example[:-5] = ", example[:-5])


print("example[-5:-5] = ", example[-5:-5])
print("example[5:-5] = ", example[5:-5])


word = "Python" # ['P', 'y', 't', 'h', 'o', 'n']
                # [ 0,   1,   2,   3,   4,   5 ]

num_one = "one"
num_two = "two"
num_three = "three"

nums = [num_one, num_two, num_three]
print(nums[0])
print(nums[1])
print(nums[2])

example = "one, two, three".split("e")

print("example[0] =", example[0])
print("example[1] =", example[1])
print("example[2] =", example[2])
print("example[3] =", example[3])

example = "one, three, two".split("e")

print("len(example) = ", len(example))

print("example[0] =", example[0])
print("example[1] =", example[1])
print("example[2] =", example[2])
print("example[3] =", example[3])

example = "one, two, three".split("e") # ["on", ", two, thr", "", ""]

print("len(example) = ", len(example))
print("example[0] =", example[0])
print("example[1] =", example[1])
print("example[2] =", example[2])
print("example[3] =", example[3])

food_list = ["apples", "bananas", "carrot", "candies", "cheese"]

food = " ".join(food_list)

print("food = ", food)
print(len(food))

# Исходные данные 5:
title_1 = "Сто лет одиночества"
title_2 = "Зеленая тетрадь"
title_3 = "Пикник на обочине"

author_1 = "Габриэль Гарсия Маркес"
author_2 = "Олег Рой"
author_3 = "Братья Стругацкие"

year_1 = 1967
year_2 = 2021
year_3 = 1972

print("%-30s|%-30s|%10s|"  %("title:", "author:","year:"))
print("%-30s|%-30s|%10d|"  %(title_1, author_1, year_1))
print("%-30s|%-30s|%10d|"  %(title_2, author_2, year_2))
print("%-30s|%-30s|%10d|"  %(title_3, author_3, year_3))