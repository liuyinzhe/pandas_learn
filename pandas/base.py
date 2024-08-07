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

# 无表头文件，添加表头
df = pd.read_csv('data.csv', sep='\t',header=None, names=['year','x1','x2','x3'])

# 转置
# df.T

# 只读取特定列 
usecols_lst = ["NO1","NO2","NO3"]
multianno_snp_df = pd.read_csv('multianno.txt',
                               sep='\t',encoding='utf-8',usecols=usecols_lst)

# 读取内容全部自定义为字符串类型
data = pd.read_csv('multianno.txt',sep='\t', dtype=str,na_values="") #na_values 避免缺失值 NaN
print(data)

# 读取CSV文件，将第一列和第三列转换为整数/浮点，第二列转换为字符串
data = pd.read_csv('yourfile.csv', dtype={0: int, 2: float, 1: str})

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


# 保存, sep 分隔符，encoding 编码，index 是否保存行索引，header 是否保存列名，columns 指定保存的列
dataframe_df.to_csv("test.csv", sep='\t',encoding="utf-8", index=False, header=True , columns=["animal", "age"])


################################# 字典转为dataframe  #########################
# 代码来自  https://blog.csdn.net/LiuRuiaby35646/article/details/138079363
# 1.pd.DataFrame()
# 字典列表，每个字典代表一行数据
data_list_of_dicts = [
    {'Company': 'Company A', 'Employees': 120, 'Revenue': 1000},
    {'Company': 'Company B', 'Employees': 80, 'Revenue': 800},
    {'Company': 'Company C', 'Employees': 300, 'Revenue': 1500}
]

# 直接将字典列表转换为DataFrame
df = pd.DataFrame(data_list_of_dicts)

# 输出
'''
     Company  Employees  Revenue
0  Company A        120     1000
1  Company B         80      800
2  Company C        300     1500
'''

# 2.pd.DataFrame.from_dict()
# (1) orient='columns' 默认
data_dict = {
    'Company': ['A', 'B', 'C'],
    'Revenue': [100, 150, 200],
    'Employees': [50, 60, 70]
}

df = pd.DataFrame.from_dict(data_dict)
print(df)
'''
  Company  Revenue  Employees
0       A      100         50
1       B      150         60
2       C      200         70

'''
# (2) orient='index'
data_dict = {
    'row1': {'Company': 'A', 'Revenue': 100, 'Employees': 50},
    'row2': {'Company': 'B', 'Revenue': 150, 'Employees': 60},
    'row3': {'Company': 'C', 'Revenue': 200, 'Employees': 70}
}

df = pd.DataFrame.from_dict(data_dict, orient='index')
print(df)
'''
      Company  Revenue  Employees
row1       A      100         50
row2       B      150         60
row3       C      200         70
'''

#4.concat()方法将字典转换为 DataFrame 行   根据相同列名合并

data_dict = {'Column1': 'Value1', 'Column2': 'Value2', 'Column3': 'Value3'}

dict_df = pd.DataFrame([data_dict])

'''
        Column1	        Column2	       Column3
0	    Value1	         Value2     	Value3
'''
# Now, create an example existing DataFrame to concatenate with.
existing_df = pd.DataFrame({
    'Column1': ['ExistingValue1', 'ExistingValue2'],
    'Column2': ['ExistingValue3', 'ExistingValue4'],
    'Column3': ['ExistingValue5', 'ExistingValue6']
})

'''
        Column1	        Column2	       Column3
0	ExistingValue1	ExistingValue3	ExistingValue5
1	ExistingValue2	ExistingValue4	ExistingValue6
'''

concatenated_df = pd.concat([existing_df, dict_df], ignore_index=True)

# Display the concatenated DataFrame
print(concatenated_df)
'''
        Column1	        Column2	       Column3
0	ExistingValue1	ExistingValue3	ExistingValue5
1	ExistingValue2	ExistingValue4	ExistingValue6
2	    Value1	         Value2     	Value3
'''
# 代码来自  https://blog.csdn.net/LiuRuiaby35646/article/details/138079363
################################# 字典转为dataframe  #########################

