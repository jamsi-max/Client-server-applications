# 1. Задание на закрепление знаний по модулю CSV.
# Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и 
# формирующий новый «отчетный» файл в формате CSV.
# Для этого:
# * Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и 
# считывание данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь 
# значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого 
# параметра поместить в соответствующий список. Должно получиться четыре списка — например, os_prod_list, 
# os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для хранения данных 
# отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», 
# «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить 
# в файл main_data (также для каждого файла);
# * Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение 
# данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
# * Проверить работу программы через вызов функции write_to_csv().
import csv
import re


file_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']

def get_data(file_list):
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы'],]

    for item in file_list:
        data = []
        create_system = []
        name_os = []
        code_prod = []
        sys_type = []

        with open(item) as file:
            for line in file:
                spam = re.findall(r'^Изготовитель системы:\s+(.+$)', line)
                if spam:
                    create_system.append(*spam)
                spam = re.findall(r'^Название ОС:\s+(.+$)', line)
                if spam:
                    name_os.append(*spam)
                spam = re.findall(r'^Код продукта:\s+(.+$)', line)
                if spam:
                    code_prod.append(*spam)
                spam = re.findall(r'^Тип системы:\s+(.+$)', line)
                if spam:
                    sys_type.append(*spam)

            data.append(*create_system)
            data.append(*name_os)
            data.append(*code_prod)
            data.append(*sys_type)

            main_data.append(data)

    with open('main_data.txt', 'w', encoding='utf-8') as main_file:
        main_file.write(str(main_data))
    
    return main_data


def write_to_csv(file_name):
    with open(file_name, 'w') as file:
        csv_file = csv.writer(file)
        for line in get_data(file_list):
            csv_file.writerow(line)


if __name__ == "__main__":
    write_to_csv('file_csv.csv')
