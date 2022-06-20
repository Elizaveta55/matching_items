import pandas as pd
import re

ksr = pd.read_csv('KSR.csv')
how_close = 0.15

def find_in_ksr(item_name):
    item_name = re.sub(r'[^\w\s]', ' ', item_name.lower())
    best_close = 0
    best_number = None
    best_name = None
    words = item_name.split(' ')
    words = list(filter(None, words))
    for item in ksr.iloc():
        temp_name = re.sub(r'[^\w\s]', ' ', item['1'].lower())
        words_item = temp_name.split(' ')
        words_item = list(filter(None, words_item))
        if len(list(set(words) & set(words_item)))/len(words) >= how_close and len(list(set(words) & set(words_item)))/len(words) > best_close:
            best_close = len(list(set(words) & set(words_item))) / len(words)
            best_number = item['0']
            best_name = item['1']
    return best_number, best_name

answer = []

orders = pd.read_csv('orders.csv')

for item in orders.iloc():
    nomer_ksr, name_ksr = find_in_ksr(item['Наименование позиции в счете'])
    name_order = item['Наименование позиции в счете']
    name_order_fact = item['Наименование позиции в заявке']
    date_1 = item['Дата счета']
    cost_date_1 = item['Стоимость позиции']
    date_2 = None
    cost_date_2 = None
    date_3 = None
    cost_date_3 = None

    answer_item = (nomer_ksr, name_ksr, name_order, name_order_fact, date_1, cost_date_1, date_2, cost_date_2, date_3, cost_date_3)
    answer.append(answer_item)
    print(answer_item)

data = pd.DataFrame(answer)
data.to_excel('answer_match.xlsx', index=None)