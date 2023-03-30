# Задача No25. Решение в группах
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз 
# каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# words = input("Введите символы через пробел: ")
# massive = words.split()

# print(massive)
# mainDigit = ""
# multiply = set()

# for i in range(len(massive)):
#     mainDigit = massive[i]
#     if mainDigit not in multiply:
#         multiply.add(mainDigit)
#         count = 0
#         for j in range(i+1, len(massive)):
#             if mainDigit==massive[j]:
#                 count = count +1
#                 massive[j] = f"{massive[i]}_{count}"

# print(massive)

# Задача No27. Решение в группах
# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells 
# I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

# n = str.split(input("Введите текст: "))
# print(f"Количество слов в тексте {len(n)}")

# 1. Задайте список из нескольких чисел. Напишите программу,
# # которая найдёт сумму элементов списка,
# # стоящих на нечётной позиции.

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import random

# massive = list()
# len = int(input("Введите длину массива:"))
# for i in range(len):
#     massive.append(random.randint(1,10))

# print(massive)
# sum = 0
# for i in range(1,len,2):
#     sum += massive[i]

# print(sum)

# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# import random

# massive = list()
# len = int(input("Введите длину массива:"))
# for i in range(len):
#     massive.append(random.randint(1,10))

# print(massive)

# newMassive = list()
# count = len//2 + int(len%2 != 0)
# for i in range(count):
#     newMassive.append(massive[i]*massive[len-1-i])

# print(newMassive)

# 3. Перемешать список заданый произвольно. [2,5,7,8] to [2,7,5,8]

import random

massive = list()
len = int(input("Введите длину массива:"))
for i in range(len):
    massive.append(random.randint(1,10))
print(massive)

newMassive = list()
x = random.randint(1,10)

for i in range(len):
    while x not in massive:
        x = random.randint(1,10)
    newMassive.append(x)
    massive.remove(x)

print(newMassive)
