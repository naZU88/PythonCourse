#найти наибольшее из двух
"""
a= int(input("число А "))

b= int(input("число Б "))

if a > b:
    print(f"{a}>{b}")
elif a == b:
    print(f"{a}={b}")
else:
    print(f"{b}>{a}")
"""


"""За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
Input:
n = 700 m = 750 Output: 2

d = int(input("Введите кол-во к/д"))
l = int(input("Введите длину маршрута"))

resultDays = l//d + (l%d/10) +0.4

resultDays = round(resultDays)
print(f"Чтобы проехать маршрут нужно {resultDays} дней")
"""

"""
Задача No3. Решение в группах
В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.
Input: 20 21 22(ввод чисел НЕ в одну строку) Output: 32


a = int(input("Введите кол-во учеников в первом классе"))
b = int(input("Введите кол-во учеников во втором классе"))
c = int(input("Введите кол-во учеников в третьем классе"))

sum = a+b+c
result = sum//2 + sum%2/10 + 0.5
result = round(result)

print(f"Кол-во необходимых парт = {result}")
"""

"""
Задача No5. Решение в группах
Вагоны в электричке пронумерованы натуральными числами, 
начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда, 
а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка). 
В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил, 
что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке. 
Напишите программу, которая будет это делать или сообщать, что без дополнительной информации это сделать невозможно.

Input: 3 4(ввод на разных строках) Output: 6
"""
i = int(input('В какой вагон по счету сел Витя? '))
j = int(input('Какой номер написан в вагоне? '))
if i != j:
print(f'В поезде {i + j - 1} вагонов.')
else:
print('Без дополнительной информации определить число вагонов невозможно.')


"""
Задача No7. Решение в группах
Дано натуральное число. Требуется определить, является ли год с данным номером високосным. 
Если год является високосным, то выведите YES, иначе выведите NO. 
Напомним, что в соответствии с григорианским календарем, год является високосным, если его номер кратен 4, 
но не кратен 100, а также если он кратен 400.

Input: 2016 Output: YES
"""

year = int(input("Введите год: "))

if (year%4 == 0 and year%100 != 100) or year%400==0:
    print("YES")
else: 
    print("NO")