import pandas as pd
import numpy as np
import os

os.chdir(r'E:\Carho\课程\数据可视化\作业\fig3')
data_filename = '工作簿1.xlsx'

#%%
data = pd.read_excel(data_filename)

#%%
data['year'] = data['date'].apply(lambda x: x.year)
data['month'] = data['date'].apply(lambda x: x.month)
grouped = data['date'].groupby([data['year'], data['month']])
last_day = grouped.max().to_list()
# data.drop(['year', 'month'], axis=1, inplace=True)
print(last_day)

#%%
data2 = pd.DataFrame(columns=data.columns)
for day in last_day:
    data2 = pd.concat([data2, data[data['date']==day]], ignore_index=True)

#%%
import matplotlib.pyplot as plt
plt.ion()
plt.scatter(x=range(len(data2['close'].values)), y=data2['close'].values)
plt.show()

#%%
data2.to_csv('bitcoin_month.csv')