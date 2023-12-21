# #task 1
# a = 2
# b = 4
# c = 8
# if a < 0:
#     print(True)
# elif b < 0:
#     print(True)
# elif c < 0:
#     print(True)
# else:
#     print(False)

# task 2
# numb = 4 - 6
# if numb % 2 == 0:
#     print("Имеют одинаковую чётность")
# else:
#     print("Нет, имеют разную чётность")

# task 3
# number = [8, 5, 10]
# print(sum([1 - x % 2 for x in number]))

# task 4
# num = int(input("Введите число: "))
# while num:
#     num1 = num % 10
#     num2 = num // 10
#     num = num1 + num2
#     if num >= 10:
#         print("Да, число двухзначное")
#     else:
#         print("Нет, число не двухзначное")
#     break


# task 5
# x = "10"
# for numb in range(20):
#     print(x)
#
# task 6
# cub = 1
# for x in range(21):
#     cub = x ** 3
#     print(cub, end=',')

# task 7
# d = 1
# for number in range(5,21):
#     d *= number
# print(d)

# task 8
# n = [1,4,9,16,25]
# for min in n:
#     if min < 13:
#         print(min)

# task 9
# s = 983568568
# min_numb = 9
# for numb_min in str(s):
#     if int(numb_min) < min_numb:
#         min_numb = int(numb_min)
#         print(min_numb)

# task 10
# def is_year_leap(year):
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
# print(is_year_leap(year=2048))

# task 11
# n = input("Введите число: ")
# n = int(n)
# def skloniaem_slovo(n):
#     if n % 10 == 1 and n % 100 != 11:
#         return "Корова"
#     elif n % 10 in [2, 3, 4] and n % 100 not in [12, 13, 14]:
#         return "Коровы"
#     else:
#         return "Коров"
# for x in range(1, n+1):
#     print(f"На лугу {x} {skloniaem_slovo(x)}")

# task 12
# def fibonacci_number(v):
#     if v <= 1:
#         return v
#     else:
#         return fibonacci_number(v-1) + fibonacci_number(v-2)
# print(fibonacci_number(10))

# task 13
# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))
# res = a
# while res % b != 0:
#     res += a
# print(res)