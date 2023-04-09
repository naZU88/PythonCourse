# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его 
# кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, 
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с 
# ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

alphv = ('а', 'е', 'ё', 'и', 'о', 'у', 'э', 'ю', 'я')
frase = (input("Введите фразу: ")).split()
print(frase)

def getQuan(word):
    count = 0
    word = list(word)
    for i in word:
        if i in alphv:
            count += 1
    return count

frase = list(map(getQuan, frase))
if sum(frase)/len(frase) == frase[0]:
    print('Парам пам-пам')
else:
    print('Пам парам')


# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть 
# распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: 
# бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# *Пример:*
# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

# def print_operation_table(operation, num_rows, num_columns):
#     arr = list()



def operation(num_rows, num_columns):
    mainArr = []
    for i in range(1, num_columns+1): 
        shortArr = []
        number = i
        for j in range(1, num_rows+1):
            shortArr.append(number)
            number += i
        mainArr.append(shortArr)
    return mainArr

def print_operation_table(operation, num_rows, num_columns):
    mainArr = operation(num_rows, num_columns)
    for i in mainArr: 
        for j in i: 
            print(j, end=' ') 
        print()

num_rows = int(input("Введите кол-во строк: "))
num_columns = int(input("Введите кол-во столбцов: "))

print_operation_table(operation, num_rows, num_columns)