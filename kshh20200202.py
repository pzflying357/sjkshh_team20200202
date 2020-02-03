# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from pandas import Series

f=open('D:/pystudy/数据可视化小组/task_1_zhaopin_data.csv',encoding='utf-8')
df1 = pd.read_csv(f)
#print(df1)
f.close()

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 300)
print(df1)
print(df1.head())
print(df1.tail())
print(df1.head(3))
print(df1.iloc[2])

print(df1.loc[:,['学历要求','工作经验','是否全职']])

df2 = df1.set_index("公司名")
print(df2)

df3=df2.drop(columns=["其他备注"])
print(df3)

df4=df3.drop('上海蜗兴科技有限公司')
print(df4)
df4.to_csv('D:/pystudy/数据可视化小组/task_1_zhaopin_data_update.csv')




