# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * ... * N 
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# Input: 5
# Output: 120

# n = int(input("Введите неотрицательное число: "))
# if n == 0:
# print("1")
# while n:
# factorial *= n
# n-=1

# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Input: 5 Output: 6

# a = int(input("Введите положительное число: "))
# count = 3
# fibonachi = -1
# c = 1
# d = 1
# while fibonachi < a:
# fibonachi = c + d
# c = d
# d = fibonachi
# count += 1

# if fibonachi == a:
# print(count)
# else:
# print(-1)

# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель 
# за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, 
# занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. 
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. 
# Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10 Output: 2

# n = int(input("Введите количество дней от 1 до 100: "))
# count = 0
# days = 0
# maxDays = 0
# while count < n:
# temp = random.randint(-50, 50)
# if temp > 0:
# days += 1

# if maxDays < days:
# maxDays = days

# else:
# days = 0
# print(temp, end=" ")
# count += 1
# print(f"Максимальная оттепель = {maxDays}")

# Задача No15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов 
# слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. 
# Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9 Output: 1 9
