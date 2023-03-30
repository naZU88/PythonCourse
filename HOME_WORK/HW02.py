# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх 
# одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Введите кол-во монеток: "))

count_y = 0
count_r = 0

for i in range(n):
    side = int(input("Введите сторону монетки через 0 и 1, где 0 - это решка, а 1 - орел: "))
    if side==0:
        count_r = count_r+1
    else:
        count_y = count_y+1

if count_r>count_y :
    print(count_y)
else:
    print(count_r)



# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.


import random

s = int(input("Введите сумму: "))
p = int(input("Введите произведение: "))

x = 0 
y = 0

while (s != x+y) or p != (x*y):
    x = random.randint(0, s)
    y = random.randint(0, s)
else:
    print(f"{x}, {y}")

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Введите число: "))
i = 0

while 2 ** i <= n:
    print(2 ** i)
    i += 1