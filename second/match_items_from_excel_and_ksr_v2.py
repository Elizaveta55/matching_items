import pandas as pd
import re

ksr = pd.read_csv('KSR.csv')
how_close = 0.15


def find_in_ksr(item_name):
    item_name = re.sub(r'[^\w\s]', ' ', item_name.lower())
    best_close = 0
    best_number = None
    best_name = None
    best_coef = 1
    reason = None
    words = item_name.split(' ')
    words = list(filter(None, words))
    for item in ksr.iloc():
        temp_name = re.sub(r'[^\w\s]', ' ', item['1'].lower())
        words_item = temp_name.split(' ')
        words_item = list(filter(None, words_item))
        if len(list(set(words) & set(words_item))) / len(words) >= how_close and len(
                list(set(words) & set(words_item))) / len(words) > best_close and (words_item[0] in words[0]):
            best_close = len(list(set(words) & set(words_item))) / len(words)
            best_number = item['0']
            best_name = item['1']
            coef = re.findall(r'\d+', item['2'])
            if coef:
                best_coef = coef[0]
        elif len(list(set(words) & set(words_item))) / len(words) >= how_close and len(
                list(set(words) & set(words_item))) / len(words) > best_close:
            reason = "Много совпадающих слов, но определяющее(=первое) не совпадает"
        elif words_item[0] == words[0]:
            reason = "Атрибуты значительно отличаются в двух позициях"
    if best_number == None:
        reason = "Не найден"
    return best_number, best_name, best_coef, reason


answer = []
answer_found = []
answer_not_found = []

orders = pd.read_csv('orders.csv')

i_flag_to_save = 0
for item in orders.iloc():
    nomer_ksr, name_ksr, coef, reason = find_in_ksr(item['Наименование позиции в счете'])
    name_order = item['Наименование позиции в счете']
    name_order_fact = item['Наименование позиции в заявке']
    date_1 = item['Дата счета']
    cost_date_1 = item['Стоимость позиции']
    date_2 = None
    cost_date_2 = None
    date_3 = None
    cost_date_3 = None

    if nomer_ksr == None:
        answer_item = (
        reason, name_order, name_order_fact, date_1, cost_date_1, date_2, cost_date_2, date_3, cost_date_3)
        answer_not_found.append(answer_item)
    else:
        answer_item = (
        nomer_ksr, name_ksr, name_order, name_order_fact, date_1, cost_date_1 / int(coef), date_2, cost_date_2, date_3,
        cost_date_3)
        answer_found.append(answer_item)
    print(answer_item)
    i_flag_to_save += 1
    if i_flag_to_save % 500 == 0:
        data = pd.DataFrame(answer_found)
        data.to_excel('answer_found.xlsx', index=None)

        data_not = pd.DataFrame(answer_not_found)
        data_not.to_excel('answer_not_found.xlsx', index=None)

data = pd.DataFrame(answer_found)
data.to_excel('answer_found.xlsx', index=None)

data_not = pd.DataFrame(answer_not_found)
data_not.to_excel('answer_not_found.xlsx', index=None)