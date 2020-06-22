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

    with open('orders.json') as fl:
        obj = json.load(fl)
        
        if not obj['orders']:
            obj['orders'].append(item)
            obj['orders'].append(quantity)
            obj['orders'].append(price)
            obj['orders'].append(buyer)
            obj['orders'].append(date)

    with open('orders.json', 'w') as fl_json:
        json.dump(obj, fl_json, indent=4)


if __name__ == '__main__':
    write_order_to_json('cup', 14, 43, 'Jony', '19.06.2020')