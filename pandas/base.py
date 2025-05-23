import pandas as pd
from pathlib import Path

example_df = pd.read_excel("人工.xlsx",sheet_name='Sheet1',index_col='编号')


#获取行索引
print(example_df.index.to_list())
#获取列索引
print(example_df.keys().to_list())

# script_path =Path(__file__)
# script_dir = Path(script_path).parent
# print(script_dir)
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

# 缺失值处理
data = pd.read_csv('multianno.txt',sep='\t', keep_default_na=False) 
# keep_default_na参数，这个参数的作用是决定要不要保留默认应该转换的缺失值列表，将这个参数设为False之后同时不定义na_values参数，就可以在读取文件时不将任何值转换为缺失值NaN

# 关闭默认的空值转换为 pd.na
data = pd.read_csv('multianno.txt',sep='\t', keep_default_na=False) 
# na_values 默认是 None ,na_values 可指定缺失值
df = pd.read_csv('file.csv', na_values=['N/A', '-', ''])
# 如果你想要指定某一列特定的空值，可以传递一个字典给na_values，其键为列名，值为空值列表：
df = pd.read_csv('file.csv', na_values={'column_name': ['N/A', '-', '']})


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
#################################  根据指定索引排序  #########################
import pandas as pd

# 创建 DataFrame
df = pd.DataFrame({
    'A': ['a', 'b', 'c'],
    'B': [1, 2, 3]
}, index=[0, 1, 2])

# 重新索引行
df_reindexed = df.reindex(index=[2, 1, 0, 3])
print(df_reindexed)

# 重新索引列
df_reindexed_columns = df.reindex(columns=['B', 'A', 'C'])
print(df_reindexed_columns)

# 填充缺失值
df_reindexed_fill = df.reindex(index=[2, 1, 0, 3], fill_value=0)
print(df_reindexed_fill)

DataFrame.reindex 支持两种调用约定：
#DataFrame.reindex(index=index_labels, columns=column_labels,...)
#DataFrame.reindex(labels, axis={'index', 'columns'},...)
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

# 长度不同的字典元素 ，转为 dataframe

def nan_fill(dic):
    '''
    dic= {
        'a':[1,2,3],
        'b':[5,],
        'c':[4,6,7,8]
        }
    '''
    max_len = max([len(v) for v in dic.values()])
    for k in dic:
        lst_len = len(dic[k])
        if len(dic[k]) < max_len:
            dic[k] += [pd.NA,]*(max_len-lst_len)
    return dic

data_dic = {'A': [1, 2],
        'B': [3, 4, 5],
        'C': [6, 7, 8, 9, 10]
        }

new_data_dic = nan_fill(data_dic)
venn_plot_df = pd.DataFrame(new_data_dic)
# 不修改 data_dic
# 通过 orient 设置key 作为行index, 数值转置后，重新设置key,由于是自定义的，key顺序固定
venn_plot_df = pd.DataFrame(pd.DataFrame.from_dict(data_dic, orient='index').values.T, columns=list(data_dic.keys()))
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
# 筛选行中0出现小于4次的内容
df_filtered = counts_df[(counts_df == 0).sum(axis=1) < 4]
####################### 多条件 apply ##########################
# 创建示例DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
})
 
# 定义条件判断函数
def condition_check(row,num_lst):
    if int(row['A']) in num_lst:
        return 'Condition met'
    if row['A'] > 2 and row['B'] > 20:
        return 'Condition met'
    else:
        return 'Condition not met'
num_lst = [3,4,5]
# 应用条件判断函数到DataFrame的Result列中
df['Result'] = df.apply(condition_check,args=(num_lst,), axis=1)



def condition_check_filter(row,num_lst):
    if int(row['A']) in num_lst:
        return True
    if row['A'] > 2 and row['B'] > 20:
        return True
    else:
        return False
num_lst = [3,4,5]
# 条件筛选符合条件的行
new_df = df[df.apply(condition_check_filter,args=(num_lst,), axis=1)]

####################### 多条件 apply ##########################

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


################################ dataframe drop删除指定列 #####################################

'''
DataFrame.drop(
     labels=None,   # labels:要删除的行或列的标签
     axis=0,        # axis:删除行还是列。0或'index'表示删除行,1或'columns'表示删除列
     index=None,    # 要删除的行标签
     columns=None,  # 要删除的列标签
     level=None,    # 用于多级索引
     inplace=False, # 是否在原地修改数据。如果为True,则在原DataFrame上进行修改,如果为False,则返回一个新的DataFrame
     errors='raise' # 如果指定的标签不存在,如何处理。'raise'表示抛出错误,'ignore'表示忽略
     )
'''

# 删除指定行
df.drop('行索引名', axis=0, inplace=True) # axis=0表示行，inplace=True表示在原数据上进行操作
# 删除多个指定列
df.drop(['列索引名1', '列索引名2'], axis=1, inplace=True) # axis=1表示列，inplace=True表示在原数据上进行操作
# 按照位置删除第二列和第三列
df.drop(df.columns[1:3], axis=1, inplace=True) # axis=1表示列，inplace=True表示在原数据上进行操作
# 按照位置删除第二行和第三行
df.drop(df.index[1:3], axis=0, inplace=True) # axis=0表示行，inplace=True表示在原数据上进行操作
# 按照 行index 删除
df.drop(index=df.index[[1,3,5]])
df.drop(df.index[[1,3,5]])

################################ dataframe drop删除指定列 #####################################

################################ dataframe 提取指定列作为新的dataframe #####################################
new_genes_df = gene_df[['Gene', 'GeneName']].copy()

# 提取指定列作为新的 DataFrame
df1_new = df1[['Gene', 'GeneName']]
df2_new = df2[['Gene', 'GeneName']]

# 合并两个 DataFrame
merged_df = pd.concat([df1_new, df2_new], ignore_index=True)

################################ dataframe 提取指定列作为新的dataframe #####################################


################################  groupby #################################################

# https://zhuanlan.zhihu.com/p/101284491
# 计算每一列相同ID的sum总和
df = pd.read_csv("format.txt",encoding="utf-8",sep='\t',index_col=None)
new_df = df.groupby('ID',as_index=False).sum()
new_df.to_csv("format.sum.txt",sep='\t',encoding="utf-8", index=False, header=True)

################################  groupby #################################################

################################ 自定义函数  ##################################################
# 定义转换函数
def convert2numeric(column,column_names_lst):
    if column.name in column_names_lst:  # 根据列名指定转换
        return pd.to_numeric(column, errors='coerce')
    else:
        return column

# 空表头文件添加表头
columns_lst = [  'CNV type', 'CNV region', 'CNV size', 'CNV level',
            'p_val', 'p_val_2', 'p_val_3', 'p_val_4', 
            'q0', 'pN', 'dG']
df = pd.read_csv("input.tsv",sep='\t',header=None,names=columns_lst)

# 'CNV type', 'CNV region', 两列不做处理
column_names_lst = ['CNV size', 'CNV level', 'p_val', 'p_val_2', 'p_val_3', 'p_val_4', 'q0', 'pN', 'dG']
# df.apply(errors='coerce')空值则返回 Na
df = df.apply(convert2numeric,args=(column_names_lst,))
print(df)
############################## 自定义函数  ##################################################

############################## 判断段字符串适合的数字类型  ##################################################
import pandas as pd
 
def get_numeric_type(s):
    try:
        pd.to_numeric(s, downcast='signed')
        return 'integer' if s.isdigit() else 'float'
    except ValueError:
        return 'non-numeric'
 
# 示例数据
data = ['1', '2.5', 'three', '4e2', '5e-1']
df = pd.DataFrame({'value': data})
 
# 判断每个字符串最适合转换的数字类型
df['numeric_type'] = df['value'].apply(get_numeric_type)
print(df)
'''
   value numeric_type
0      1      integer
1    2.5        float
2  three  non-numeric
3    4e2        float
4   5e-1        float
'''
############################## 判断段字符串适合的数字类型  ##################################################

###################### 创建多个新列，逐行修改每个值  ##################################
# 创建新的列来存储解析后的分类信息
new_columns = ['kingdom', 'phylum', 'class', 'order', 'family', 'genus', 'species']
for col in new_columns:
    df[col] = None

# 遍历 'taxonomy' 列并使用 taxonomy_parser 函数解析
for index, row in df.iterrows():
    if pd.notna(row['taxonomy']):
        parsed_taxonomy = taxonomy_parser(row['taxonomy'], db_type="Silva")  # 根据实际情况选择数据库类型
        for i, col in enumerate(new_columns):
            # print(i, col) 迭代每个 新列名，将每行对应的新列明 单个元素进行修改
            df.at[index, col] = parsed_taxonomy[i]
###################### 遍历中，逐行修改每个值at  ##################################
import pandas as pd

# 创建一个示例 DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10]}
df = pd.DataFrame(data)

# 遍历 DataFrame 的行
for index, row in df.iterrows():
    # 根据行中数值修改列 'A' 的值
    if row['A'] > 3:
        df.at[index, 'A'] = row['A'] * 2

print(df)
##########################################################################################
