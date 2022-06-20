import pandas as pd

data = pd.read_excel('answer_fixed_cost.xlsx')
name_order = data[2].tolist()
name_order_fact = data[2].tolist()

time_distributed = []
for item in data.iloc():
    top_found = data.loc[data[2] == item[2]]
    if len(top_found)>1:
        nomer_ksr = top_found[0].mode()
        if nomer_ksr.empty:
            nomer_ksr = None
        name_ksr = top_found[1].mode()
        if name_ksr.empty:
            name_ksr = None
        name_order = item[2]
        name_order_fact = item[3]
        item_time_distributed = [nomer_ksr, name_ksr, name_order, name_order_fact]
        for row in top_found.iloc():
            date = row[4]
            cost_date = row[5]
            item_time_distributed.append(date)
            item_time_distributed.append(cost_date)
        time_distributed.append(item_time_distributed)
    else:
        time_distributed.append(list(item))

print(time_distributed)
data_time_distributed = pd.DataFrame(time_distributed)
data_time_distributed.to_excel('answer_fixed_date.xlsx', index=None)