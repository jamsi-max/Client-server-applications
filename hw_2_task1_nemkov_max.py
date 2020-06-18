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


def write_file(data_list):
    with open('main_data.txt', 'a') as file:
        for item in data_list:
            file.write(item+',')
        file.write('\n')


def get_data(file_list):
    main_data = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    create_system = []
    name_os = []
    code_prod = []
    sys_type = []

    for item in file_list:
        with open(item) as file:
            for line in file:
                data_1 = re.findall(r'^Изготовитель системы:\s+(.+$)', line)
                data_2 = re.findall(r'^Название ОС:\s+(.+$)', line)
                data_3 = re.findall(r'^Код продукта:\s+(.+$)', line)
                data_4 = re.findall(r'^Тип системы:\s+(.+$)', line)

                if data_1:
                    create_system.append(*data_1)
                elif data_2:
                    name_os.append(*data_2)
                elif data_3:
                    code_prod.append(*data_3)
                elif data_4:
                    sys_type.append(*data_4)

    write_file(main_data)
    write_file(create_system)
    write_file(name_os)
    write_file(code_prod)
    write_file(sys_type)


if __name__ == "__main__":
    get_data(file_list)
