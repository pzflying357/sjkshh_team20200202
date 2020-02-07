# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from pandas import Series
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['KaiTi']
mpl.rcParams['font.serif'] = ['KaiTi']
#1
f=open('D:/pystudy/数据可视化小组/task_3.1_zhihu_timeline_answer.csv',encoding='utf-8')
zhihu_data_answer = pd.read_csv(f)
#print(zhihu_data_answer)
f.close
print(zhihu_data_answer.head())
#df1 = zhihu_data_answer.groupby('回答点赞数')('回答感谢数')
#2
x=zhihu_data_answer['回答点赞数'].values.tolist()
y=zhihu_data_answer['回答感谢数'].values.tolist()
# ax.set(title='回答点赞数和感谢数散点图',xlabel=('回答点赞数'),ylabel=('回答感谢数'))
plt.xlabel('回答点赞数')
plt.ylabel('回答感谢数')
plt.title('回答点赞数和感谢数散点图')
#画散点图
plt.scatter(x,y,c = 'red',marker = '.')
#显示所画的图
plt.show()
#df1 = zhihu_data_answer.groupby('回答点赞数')('回答感谢数')
#3
x=zhihu_data_answer['问题回答数'].values.tolist()
y=zhihu_data_answer['问题关注数'].values.tolist()
# ax.set(title='回答点赞数和感谢数散点图',xlabel=('回答点赞数'),ylabel=('回答感谢数'))
plt.xlabel('问题回答数')
plt.ylabel('问题关注数')
plt.title('问题回答数和关注数散点图')
#画散点图
plt.scatter(x,y,c = 'blue',marker = '.')
#显示所画的图
plt.show()
#4
f=open('D:/pystudy/数据可视化小组/task_3.2_zhihu_timeline_article.csv',encoding='utf-8')
zhihu_data_article = pd.read_csv(f)
#print(zhihu_data_answer)
f.close
print(zhihu_data_article.head())
#5
x=zhihu_data_article['文章点赞数'].values.tolist()
y=zhihu_data_article['文章评论数'].values.tolist()
# ax.set(title='文章点赞数和评论数散点图',xlabel=('文章点赞数'),ylabel=('文章评论数'))
plt.xlabel('文章点赞数')
plt.ylabel('文章评论数')
plt.title('文章点赞数和评论数散点图')
#画散点图
plt.scatter(x,y,c = 'blue',marker = '.')
#显示所画的图
plt.show()

#6
x = zhihu_data_article['文章点赞数'].values.tolist()
x1 = [i for i in x if i<1000]
plt.boxplot(x1)
plt.show()