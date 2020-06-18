# 2. Задание на закрепление знаний по модулю json.
# Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий его 
# заполнение данными.
# Для этого:
# * Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество 
# (quantity), цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных
#  в виде словаря в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
# * Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого 
# параметра.
import json

def write_order_to_json(item, quantity, price, buyer, date):
    order = {
        'order': [
            item,
            quantity,
            price,
            buyer,
            date
        ],
    }

    with open('orders.json', 'a') as fl_json:
        json.dump(order, fl_json, indent=4)


if __name__ == '__main__':
    write_order_to_json('cup', 14, 43, 'Jony', '19.06.2020')