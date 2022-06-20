import pandas as pd
import re

answer = pd.read_excel('answer_not_found.xlsx')
# answer = pd.read_excel('answer_found.xlsx')
orders = pd.read_csv('orders.csv')
answer_fixed_cost = []
for item in answer.iloc():
    top_found = orders.loc[(orders['Наименование позиции в счете'] == item[1]) &
                           (orders['Наименование позиции в заявке'] == item[2])]
    try:
        item[4] = int(top_found.iloc()[0]['Стоимость позиции'])/int(top_found.iloc()[0]['Кол-во позиций в счете'])
    except ZeroDivisionError:
        item[4] = "Проверьте количество"
    answer_fixed_cost.append(item)

data = pd.DataFrame(answer_fixed_cost)
data.to_excel('answer_not_found_fixed_cost.xlsx', index=None)