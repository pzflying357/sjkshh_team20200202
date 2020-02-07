# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from pandas import Series
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['KaiTi']
mpl.rcParams['font.serif'] = ['KaiTi']


f=open('D:/pystudy/数据可视化小组/task_2_lianjia_data.csv',encoding='utf-8')
lianjia_data = pd.read_csv(f)
#print(df1)
f.close

print(lianjia_data.head())
fy_count1 = [('房源数量','count')]
df1 = lianjia_data.groupby('面积大小（㎡）')['面积大小（㎡）'].agg(fy_count1)

#df2.to_csv('D:/pystudy/数据可视化小组/task2_data_update.csv')
#print(df2.head())

x=df1.index.values.tolist()
y1=df1['房源数量'].values.tolist()
y2=df1['房源数量'].values.tolist()

plt.plot(x, y1,color='green', marker='.', linestyle='dashed', linewidth=1, markersize=6)
plt.bar(x, y2, width=0.8, color='blue', edgecolor='white', label='房源数量')
plt.legend(loc="upper right")
# ax.set(title='各面积的房源数量', xlabel='面积大小（平方米）', ylabel='房源数量')
plt.tick_params(labelsize=14)
plt.xlabel('面积大小（平方米）')
plt.ylabel('房源数量')
plt.title('各面积的房源数量')
plt.show()

#结论 房源数量主要集中在面积在25-60平方米之间，面积在100平米以上或15平方米以下的的房源数量较少。
fy_count2 = [('房源数量','count')]
df2 = lianjia_data.groupby('区')['区'].agg(fy_count2)
x=df2.index.values.tolist()
y1=df2['房源数量'].values.tolist()
# ax.set(title='各区房源数量', xlabel='区', ylabel='房源数量')
plt.tick_params(labelsize=8)
plt.xlabel('区')
plt.ylabel('房源数量')
plt.title('各区房源数量')
plt.bar(x, y1, width=0.8, color='red', edgecolor='white')
plt.show()

#结论 徐汇区房源数量最多，超过120个，奉贤区最少；发达区域房源数量总体在80个以上比偏远区域20个以下。

fy_count3 = [('房源数量','count')]
df3 = lianjia_data.groupby('楼层类型')['楼层类型'].agg(fy_count3)
x = df3.index.values.tolist()
#print(x)
#x1 = ''.join(x).strip().split()
x2 = [i.strip() for i in x]
#print(x1)

y1 = df3['房源数量'].values.tolist()
# ax.set(title='不同楼层房源数量', xlabel='楼层类型', ylabel='房源数量')
#plt.tick_params(labelsize=10)
#plt.xlabel('楼层类型')
#plt.ylabel('房源数量')
#plt.title('不同楼层类型房源数量')
#plt.bar(x2, y1, width=0.3, color='purple', edgecolor='white')


plt.pie(y1, labels=x2, autopct='%1.2f%%')  # 画饼图（数据，数据对应的标签，百分数保留两位小数点）
plt.title("不同楼层类型房源数量")
plt.show()

#结论 高楼层房源数量最多，占比接近一半，其次是中楼层占30%，最后是低楼层接近20%。
