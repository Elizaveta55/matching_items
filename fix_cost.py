import pandas as pd
import re

answer = pd.read_excel('answer_match.xlsx')
orders = pd.read_csv('orders.csv')
answer_fixed_cost = []
for item_1, item_2 in zip(orders.iloc(), answer.iloc()):
    try:
        item_2[5] = int(item_1['Стоимость позиции'])/int(item_1['Кол-во позиций в счете'])
    except ZeroDivisionError:
        item_2[5] = "Проверьте количество"
    answer_fixed_cost.append(item_2)

data = pd.DataFrame(answer_fixed_cost)
data.to_excel('answer_fixed_cost.xlsx', index=None)