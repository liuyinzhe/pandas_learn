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


##############################  条件筛选  #############################


#1.单条件筛选

df.loc[df['Item'] == 'Milk']
df[df["sh"]>5]
df[df["sh"].map(lambda x:x>5)]
# 字符串切片，判断
df[df["date"].map(lambda x:x[0:4])=="2019"]

#2.多条件筛选
df.loc[(df['Price'] < 2) | (df['Discount'] > 0)]

df.loc[(df['Price'] > 3) | ((df['Discount'] > 0) & (df['Unit'] == 'Dozen'))]

# 使用isin()方法筛选
df.loc[df['Item'].isin(['Milk', 'Bread'])]
df[(df['级别'].isin (['一线','二线']))]
df[((df['级别'].isin (['一线','二线']))&(df['是否沿海'].isin(['沿海'])))]

# 使用between()方法筛选
df.loc[df['Price'].between(2, 3)]
# 3.字符串条件筛选
#(1) 使用str.contains()方法筛选
'''
.str.contains()中还可以设置正则化筛选逻辑。
case=True：使用case指定区分大小写
na=True：就表示把有NAN的转换为布尔值True
flags=re.IGNORECASE：标志传递到re模块，例如re.IGNORECASE
regex=True：regex ：如果为True，则假定第一个字符串是正则表达式，否则还是字符串
'''
df.loc[df['Item'].str.contains('Bread')]
# 筛选字符串 ，正则表达式
df.loc[df['Name'].str.contains('Mrs|Lily'),:].head()
# 筛选含有“一线”或“二线”的行
df[df['级别'].str.contains("一线|二线",na=False)]
# 过滤去掉含有“一线”或“二线”的行
df[~df['级别'].str.contains("一线|二线",na=False)]

#(2) 使用str.startswith()方法筛选
df.loc[df['Item'].str.startswith('B')]
#(3) 使用str.endswith()方法筛选
df.loc[df['Item'].str.endswith('s')]
#(4) 使用str.match()方法筛选
df.loc[df['Item'].str.match('B.*s')]
#(5) 使用str.len()方法筛选
df[df['诗人'].str.len() <= 2]
#原文链接 https://blog.csdn.net/qq_41314882/article/details/134872056
#(6) df.notna() df.isna() 筛选空/非空
df[df['age'].notna()]
df[df['age'].isna()]
#(7) 正则匹配

import re
province = pd.DataFrame(['广东', '广西', '福建', '福建省'], columns=['省份'])
#自定义函数，如果包含“广”字，则返回True,否则返回False
def func(x):
    if re.search(".*广.*",x):
        return(True)
    else:
        return(False)
province[province["省份"].apply(func)]
#原文链接：https://blog.csdn.net/p1306252/article/details/114879951

'''
DataFrame.apply(
            func:function
            axis:{0 or ‘index’, 1 or ‘columns’}, default 0 
            raw:bool, default False
            result_type:{‘expand’, ‘reduce’, ‘broadcast’, None}, default None
            args:tuple) Positional arguments to pass to func in addition to the array/series.
            **kwargs Additional keyword arguments to pass as keywords arguments to func.

Returns:Series or DataFrame
Result of applying func along the given axis of the DataFrame.

DataFrame.apply(self, func, axis=0, raw=False, result_type=None, args=(), **kwds）
func 代表的是传入的函数或 lambda 表达式；
axis 参数可提供的有两个，该参数默认为0/列
0 或者 index ，表示函数处理的是每一列；
1 或 columns ，表示处理的是每一行;
raw ；bool 类型，默认为 False;
False ，表示把每一行或列作为 Series 传入函数中；
True，表示接受的是 ndarray 数据类型；
apply() 最后的是经过函数处理，数据以 Series 或 DataFrame 格式返回。
                        
原文链接：https://blog.csdn.net/weixin_60535956/article/details/136486200


'''
target_lst = ['广东', '广西', '福建', '福建省']
def func(x,lst):
    if ';' in x:
        record = re.split(";",x.strip())
        for item in record:
            if item in lst:
                return True
    else:
        if x in lst:
            return True
        else:
            return False
    # for 循环没找到，则返回 False
    return(False)
province[province["省份"].apply(func,args=(target_lst,))]


#3.df.duplicated() 重复内容筛选

df[df.duplicated(subset=["one"],keep="last")]#返回除最后一次出现的重复值
df[df.duplicated(subset=["one"],keep=False)]#返回所有重复值

#4.df.filter() 筛选
'''
items：固定列名
regex：正则表达式
like：以及模糊查询
axis：控制是行index或列columns的查询
'''
# 数据集
df = pd.DataFrame(np.array(([1, 2, 3], [4, 5, 6])),
                  index=['mouse', 'rabbit'],
                  columns=['one', 'two', 'three'])
df
'''
        one  two  three
mouse     1    2      3
rabbit    4    5      6
'''
# 按名称选择列
df.filter(items=['one', 'three'])
'''
         one  three
mouse     1      3
rabbit    4      6
'''
# 按正则表达式选择列
df.filter(regex='e$', axis=1)
'''
         one  three
mouse     1      3
rabbit    4      6
'''
# 选择包含“bbi”的行
df.filter(like='bbi', axis=0)
'''
         one  two  three
rabbit    4    5      6
'''

#5.where/mask
# where接受的条件需要是布尔类型，如果不满足匹配条件，就被赋值为默认的NaN或其他指定值
df['quality'] = '' # 额外创建的列，则会成为other的填充列，单条则填充单个条件
cond1 = df['Sex'] == 'male'
cond2 = df['Age'] > 25
 
df['quality'].where(cond1 & cond2, other=pd.NA, inplace=True)
# other 是False时，默认是 NaN填充，也可以额外指定
# mark 就是 where 的反条件

#6.query
# 常用方式
df[df.Age > 25]
# query方式
df.query('Age > 25')
df.query("Name.str.contains('William') & Age > 25")
df.query('Sex == "male" and Age > 25')

# 参考链接 https://blog.csdn.net/joker_zsl/article/details/119874694
##############################  条件筛选  #############################


############################## 条件判断添加新列 #############################

data['dd_xun'] = data['dd'].apply(lambda x: '上旬' if x<=10 else '中旬' if x<=20 else '下旬')
# 原文链接: https://blog.csdn.net/arbraham/article/details/106562601
############################## 条件判断添加新列 #############################



################################ pandas 读取 gzip 压缩表格 与 输出压缩表格 ###############################
def sv_func(x,lst):
    '''
    dataframe.apply(func, args=(lst,),axis=0)
    '''
    'SRCIN1(0;-)'
    gene_id = re.sub(r"\(\d{1,};[-+]{1,}\)","",x)
    if gene_id in lst:
        return True
    else:
        return False


df = pd.read_csv('query.tsv.gz',sep='\t',compression='gzip')
print(df['query.startfeature'].to_list())
# df.to_csv('query.tsv', index=False)
TSG_lst=['GPAT2',]
# 过滤
TSG_df = df[df["query.startfeature"].apply(sv_func,args=(TSG_lst,))]
#保存
TSG_df.to_csv('query2.csv.gz',sep='\t' ,index=False, compression='gzip')

################################ pandas 读取 gzip 压缩表格 与 输出压缩表格 ###############################
