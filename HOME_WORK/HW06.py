# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения 
# n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# firstElement = int(input("Введите первый эл-т прогрессии: "))
# diff = int(input("Введите разность: "))
# quant = int(input("Введите кол-во элементов прогрессии: "))
# arr = list()

# for i in range(1, quant+1):
#     arr.append(firstElement + (i-1)*diff)

# print(arr)

# Задача 32: Определить индексы элементов массива (списка), значения которых 
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

arr = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

min = int(input("Введите нижнюю границу: "))
max = int(input("Введите верхнюю границу: "))

newArr = list()
for i in range(len(arr)):
    if 5 < arr[i] < 15:
        newArr.append(i)

print(newArr)
