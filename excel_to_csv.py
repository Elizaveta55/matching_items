import pandas as pd

data = pd.read_excel('Позиции_заявок_и_счетов_по_проекту_Кардиология_partner_1.xlsx', converters= {'Дата счета': pd.to_datetime})

data.to_csv('orders.csv', index=None)