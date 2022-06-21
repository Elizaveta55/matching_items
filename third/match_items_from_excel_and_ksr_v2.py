import pandas as pd
import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

ksr = pd.read_csv('KSR.csv')
how_close = 35


def find_in_ksr(item_name, item_name_facto):
    item_name = re.sub(r'[^\w\s]', '', item_name.lower())
    item_name_facto = re.sub(r'[^\w\s]', '', item_name_facto.lower())
    best_close = 0
    best_number = None
    best_name = None
    reason = None
    for item in ksr.iloc():
        temp_name = re.sub(r'[^\w\s]', '', item['1'].lower())
        temp_name_first_word = temp_name.split(' ')[0]
        temp = fuzz.token_set_ratio(item_name, temp_name)
        if temp >= how_close and temp > best_close and (
                temp_name_first_word in item_name.split(' ') or temp_name_first_word in item_name_facto.split(' ')):
            best_close = temp
            best_number = item['0']
            best_name = item['1']
        elif temp < how_close and (temp_name_first_word in item_name or temp_name_first_word in item_name_facto):
            reason = "Атрибуты значительно отличаются в двух позициях"
        elif temp >= how_close and temp > best_close:
            reason = "Лидирующее слово не найдено, по аттрибутам есть совпадения"
    if best_number == None:
        reason = "Не найден"
    return best_number, best_name, reason


answer = []
answer_found = []
answer_not_found = []

orders = pd.read_csv('orders.csv')

i_flag_to_save = 0
for item in orders.iloc():
    nomer_ksr, name_ksr, reason = find_in_ksr(item['Наименование позиции в счете'],
                                              item['Наименование позиции в заявке'])
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
        nomer_ksr, name_ksr, name_order, name_order_fact, date_1, cost_date_1, date_2, cost_date_2, date_3, cost_date_3)
        answer_found.append(answer_item)
    print(answer_item)
    i_flag_to_save += 1
    if i_flag_to_save % 100 == 0:
        data = pd.DataFrame(answer_found)
        data.to_excel('answer_found.xlsx', index=None)

        data_not = pd.DataFrame(answer_not_found)
        data_not.to_excel('answer_not_found.xlsx', index=None)

data = pd.DataFrame(answer_found)
data.to_excel('answer_found.xlsx', index=None)

data_not = pd.DataFrame(answer_not_found)
data_not.to_excel('answer_not_found.xlsx', index=None)