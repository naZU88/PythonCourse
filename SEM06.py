# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, 
# в каком они идут в первом массиве), которых нет во втором массиве. Пользователь вводит число 
# N - количество элементов в первом массиве, затем N чисел - элементы массива. Затем число M - 
# количество элементов во втором массиве. Затем элементы второго массива

# def CreateMassive(text):
#     n = int(input(text))
#     massive = list()  
#     for i in range(n):
#         x = int(input("Введите элемент: "))
#         massive.append(x)
#     return massive

# arr1 = CreateMassive('Введите кол-во элементов первого массива: ')
# arr2 = CreateMassive('Введите кол-во элементов второго массива: ')

# arrFinal = list()
# for i in range(len(arr1)):
#     if arr1[i] not in arr2:
#         arrFinal.append(arr1[i])

# print(arrFinal)


# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит 
# количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в массиве Далее записаны N чисел — 
# элементы массива. Массив состоит из целых чисел.

# def CreateMassive():
#     n = int(input("Введите длину массива: "))
#     massive = list()  
#     for i in range(n):
#         x = int(input("Введите элемент: "))
#         massive.append(x)
#     return massive

# arr = CreateMassive()

# count = 0
# for i in range(1, len(arr)-1):
#     if arr[i] < arr[i-1] and arr[i]<arr[i+1]:
#         count += 1

# print(count)


# from random import randint as rnd

# n = int(input("Введите кол-во элементов в 1-м списке: "))

# list = [rnd(1, 10) for i in range(n)]

# print(list)

# cnt = 0

# for i in range(1, len(list) - 1):
#     if list[i - 1] < list[i] and list[i + 1] < list[i]:
#         cnt += 1

# print(cnt)

# Два различных натуральных числа n и m называются дружественными, если сумма делителей 
# числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – 
# дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых 
# не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 105. 
# Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k. 
# Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена 
# только один раз (перестановка чисел новую пару не дает).


# 4. Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел, делящихся на 9.
# При решении задачи используйте комбинацию функций filter, map, sum.

# Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.


# 5. Напишите функцию triangle(a, b, c), которая принимает на вход три длины отрезков и определяет, 
# можно ли из этих отрезков составить треугольник.
# Входные данные
# Выходные данные
# triangle(1, 1, 2)
# Это не треугольник
# triangle(7, 6, 10)

# a = [4, 3, -10, 1, 7, 12] —— [4, -10, 12, 3, 1, 7]

# a = [4, 3, -10, 1, 7, 12]
# a.sort(key=lambda x: x%2)
# print(a)

# Подвиг 7. Вводятся номера телефонов в одну строчку через пробел с разными кодами стран: 
# +7, +6, +2, +4 и т.д. Необходимо составить словарь d, где ключи - это коды +7, +6, +2 и т.п., 
# а значения - список номеров (следующих в том же порядке, что и во входной строке) с соответствующими кодами. 
# Полученный словарь вывести командой:

# print(*sorted(d.items()))

# Sample Input:
# +71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890
# Sample Output:
# ('+2', ['+21235777890', '+21234567110']) ('+5', ['+52134567890']) ('+6', ['+61234576890']) 
# ('+7', ['+71234567890', '+71234567854', '+71232267890'])