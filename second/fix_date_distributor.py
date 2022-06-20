import pandas as pd

data = pd.read_excel('answer_not_found_fixed_cost.xlsx')
name_order = data[1].tolist()
name_order_fact = data[2].tolist()

time_distributed = []
for item in data.iloc():
    top_found = data.loc[data[1] == item[1]]
    if len(top_found)>1:
        nomer_ksr = top_found[0].mode()
        if nomer_ksr.empty:
            nomer_ksr = None
        name_ksr = top_found[1].mode()
        if name_ksr.empty:
            name_ksr = None
        name_order = item[1]
        name_order_fact = item[2]
        item_time_distributed = [nomer_ksr[0], name_ksr[0], name_order, name_order_fact]
        for row in top_found.iloc():
            date = row[3]
            cost_date = row[4]
            item_time_distributed.append(date)
            item_time_distributed.append(cost_date)
        time_distributed.append(item_time_distributed)
    else:
        time_distributed.append(list(item))

data_time_distributed = pd.DataFrame(time_distributed)
data_time_distributed.to_excel('answer_not_found_fixed_date.xlsx', index=None)