# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и 
# проверить тип и содержание соответствующих переменных. Затем с помощью онлайн-конвертера 
# преобразовать строковые представление в формат Unicode и также проверить тип и содержимое
# переменных.
str_1 = 'разработка'
str_2 = 'сокет'
str_3 = 'декоратор'

print(type(str_1))
print(str_1)
print(type(str_2))
print(str_2)
print(type(str_3))
print(str_3)

'''преообразование через онлайн-конвертера'''
str_1 = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
str_2 = '\u0441\u043e\u043a\u0435\u0442'
str_3 = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

print(type(str_1))
print(str_1)
print(type(str_2))
print(str_2)
print(type(str_3))
print(str_3)

# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность 
# кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

str_1 = b'class'
str_2 = b'function'
str_3 = b'method'

print(type(str_1))
print(str_1)
print(len(str_1))

print(type(str_2))
print(str_2)
print(len(str_2))

print(type(str_3))
print(str_3)
print(len(str_3))

# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
# str_1= b'attribute'
# str_2 = b'класс'
# str_3 = b'функция'
# str_4 = b'type'
# str_5 = b'word'
'''невозможно записать слова в байтовом типе  "класс" и "функция"'''


# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в 
# байтовое и выполнить обратное преобразование (используя методы encode и decode).
list_str = ['разработка', 'администрирование','protocol', 'standard']
list_str = [spam.encode('utf-8') for spam in list_str]
print(list_str)
list_str = [spam.decode('utf-8') for spam in list_str]
print(list_str)


# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип
# на кириллице.
import subprocess
import chardet

# args = ['ping', 'yandex.ru']
args = ['ping', 'youtube.com']

sub_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

for line in sub_ping.stdout:
    print(line.decode(chardet.detect(line)['encoding']))


# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», 
# «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести 
# его содержимое.
from chardet.universaldetector import UniversalDetector

list_str = ['сетевое программирование', 'сокет', 'декоратор']

with open('test_file.txt', 'w', encoding='UTF-16') as file:
    for spam in list_str:
        file.write(spam+'\n')

detector = UniversalDetector() 
with open('test_file.txt','rb') as file:
    for line in file:
        detector.feed(line)
        if detector.done:
            break
    detector.close()
print(detector.result['encoding'])

with open('test_file.txt', encoding='UTF-8') as file:
    print(file.read())
'''принудительное открытие в кодировке UTF-8 выдаст ошибку если файл имеет другую кодировку'''