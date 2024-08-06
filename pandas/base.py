import pandas as pd
from pathlib import Path

example_df = pd.read_excel("人工.xlsx",sheet_name='Sheet1',index_col='编号')


#获取行索引
print(example_df.index.to_list())
#获取列索引
print(rengong_df.keys().to_list())


current_path = Path.cwd()
input_path = current_path.joinpath("a.txt")

dataframe_df = pd.read_csv(input_path,encoding="utf-8",sep='\t',index_col=None)
# print(dataframe_df.index.to_list())  # row index
# print(dataframe_df.columns.to_list()) # columns

# for column_index in dataframe_df:
#     print(column_index)


#header=0
#names=["NO1","NO2","NO3"]
# usecols=usecols_lst
# df.T
# usecols_lst = ['','']
# multianno_snp_df = pd.read_csv('_multianno.txt',
#                                sep='\t',encoding='utf-8',usecols=usecols_lst)



# 按行遍历
# for index, row in dataframe_df.iterrows():
#     print(index) # 输出每行的索引值
#     print(row) # 输出每一行
#     print(row['age'], row['sex'])  # 输出每一行指定字段值

# 按列遍历
# for index, col in dataframe_df.items():
#     #print(index) # 输出每列的索引
#     #print(col)# 输出各列
#     print(col[0], col[1], col[2])  # 输出每一列指定行号的值



# DataFrame 新增列的五种方法
# https://blog.csdn.net/qq_35318838/article/details/102720553

import pandas as pd
import numpy as np
data = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
# print(data)

'''
    a 	b 	c
0 	1 	2 	3
1 	4 	5 	6
2 	7 	8 	9
'''
# insert 方法  添加一列
data.insert(data.shape[1], 'd', 0) # 列索引，列名字，统一的列值

# obj['col'] = value 方法  直截了当添加一列
data['d'] = 0

# reindex 方法  可以指定多列，缺失值填充fill_value，需要提供所有列名
# column_index = df.columns.tolist()
# index_names = df.index.tolist()
data = data.reindex(columns=['a', 'b', 'c', 'd'], fill_value=0)

# concat 方法  dataframe 行索引 拼接
data = pd.concat([data, pd.DataFrame(columns=['d'])], sort=False)

# loc 方法  指定列名添加一列
# 固定行，列 data.loc[index, col] = value
data.loc[:, 'd'] = 0
