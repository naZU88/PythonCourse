# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
import csv

def read_csv(filename='phonebook.csv'):
    """Функция читает csv-файл и возвращает список списков - строк csv-файла."""
    with open(filename, 'r', encoding='utf-8') as file:
        data = []
        for line in file:
            # В конце каждой строки символ переноса строки '\n', удаляем его с помощью метода strip()
            # А затем с помощью метода split() делим каждую строку по запятым и результат (список)
            # помещаем в другой список - data
            data.append(line.strip('\n').split(','))
    return data


def display_all_records():
    """Функция выводит на печать содержание всего справочника в отформатированном виде."""
    data = read_csv()  # Считываем содержание справочника с помощью нашей функции read_csv и сохраняем в data
    # Перебираем наши данные построчно и выводим каждую строку в отформатированном виде:
    for row in data:
        print(f'Фамилия: {row[0]}\nИмя: {row[1]}\nНомер телефона: {row[2]}\nКомментарий: {row[3]}\n')


def find_last_name():
    """Функция запрашивает фамилию абонента, находит данные по этой фамилии и выводит их на печать."""
    last_name = input('Введите фамилию: ')
    data = read_csv()  # Считываем содержание справочника с помощью нашей функции read_csv и сохраняем в data
    # Перебираем наши данные построчно и сравниваем введенное нами last_name с нулевым элементом каждой списка
    for row in data:
        if row[0] == last_name:
            print(f'Фамилия: {row[0]}\nИмя: {row[1]}\nНомер телефона: {row[2]}\nКомментарий: {row[3]}\n')


def add_data(filename='phonebook.csv'):
    """Функция дополняет телефонный справочник данными нового абонента."""
    with open(filename, 'a', encoding='utf-8') as file:  # Открываем файл с флагом 'a' - дозапись.
        # Запрашиваем данные об абоненте, разбиваем их по запятым и помещаем в список с пом. метода split():
        info = input('Введите данные абонента (фамилия, имя, номер, комментарий - через запятую): ').split(', ')
        # Полученный список вновь собираем в строку (но без лишних пробелов около запятых),
        # добавляем перенос строки '\n' и записываем в файл:
        file.write(','.join(info) + '\n')
        print('Данные записаны.')
        # Если пользователь будет вводить данные через запятую и без пробелов, можно немного упростить:
        # info = input('Введите данные абонента (фамилия, имя, номер, комментарий - через запятую без пробела): ')
        # file.write(info + '\n')

def find_phone_number():
    """Функция запрашивает телефон абонента, находит соответствующие данные и выводит на печать"""
    phone = input('Введите номер телефона: ')
    data = read_csv()  # Считываем содержание справочника с помощью нашей функции read_csv и сохраняем в data
    # Перебираем наши данные построчно и сравниваем введенный нами phone со вторым элементом каждой списка
    for row in data:
        if row[2] == phone:
            print(f'Фамилия: {row[0]}\nИмя: {row[1]}\nНомер телефона: {row[2]}\nКомментарий: {row[3]}\n')

def delite_phone_number():
    with open('phonebook.csv', 'r+', encoding='utf-8') as file:  
        info = input('Введите данные абонента (номер - через запятую): ')
        data = list(csv.reader(file))
        user_info = list(filter(lambda x: x[0] == info, data))
        print(user_info)
        if len(user_info) > 0:
            data.remove(user_info[0])
            file.seek(0)
            csv.write(file).writerows(data)
            file.truncate()
            print("Пользователь удален")
        else:
            print("Пользователь не найден")
            
def remove_phone_number():
    with open('phonebook.csv', 'r+', encoding='utf-8') as file:  
        info = input('Введите данные абонента (номер - через запятую): ')
        data = list(csv.reader(file))
        user_info = list(filter(lambda x: x[0] == info, data))
        print(user_info)
        if len(user_info) > 0:
            Newinfo = input('Введите данные абонента (фамилия, имя, номер, комментарий - через запятую): ').split(', ')
            data.remove(user_info[0])
            file.seek(0)
            writer = csv.writer(file)
            writer.writerows(data)
            writer.writerow(Newinfo)
            print("Пользователь отредактирован")
        else:
            print("Пользователь не найден")
          

number = 0
while number != '6':
    print('Введите число для операции со справочником:')
    print('1 - вывести весь справочник;\n2 - найти абонента по фамилии;\n'
          '3 - найти абонента по номеру телефона;\n4 - ввести данные нового абонента; \n5 - удалить абонента; \n'
          '6 - отредактировать абонента; \n7 - завершить работу.')

    number = input()

    if number == '1':
        display_all_records()

    elif number == '2':
        find_last_name()

    elif number == '3':
        find_phone_number()

    elif number == '4':
        add_data()
    
    elif number =='5':
        delite_phone_number()

    elif number =='6':
        remove_phone_number()

else:
    print('Работа завершена.')