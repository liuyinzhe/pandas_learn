import pandas as pd
import sys

# 获取excel表中每个sheet的名称
# https://blog.csdn.net/xiaofeixia002X/article/details/139681205
sheet_name_lst = []
with pd.ExcelFile('group.xlsx') as excel_file:
    #print(excel_file.sheet_names)
    sheet_name_lst=excel_file.sheet_names

# 指定sheet
sheet_index = int(sys.argv[1])-1
df = pd.read_excel("group.xlsx",sheet_name=sheet_name_lst[sheet_index])

# 读取指定列名读取
usecols_name_lst = ['Chr','Start','End','Ref','Alt','Func.refGene','Gene.refGene','Otherinfo11','Otherinfo12','Otherinfo13']
test_df = pd.read_csv("test.tsv",sep='\t', usecols=usecols_name_lst) 

group_dic = {}
group_sample_order = []
# 逐行读取
for index, row in df.iterrows():
    sample_name = row['OTU']
    #print(row['OTU'],row['group'])
    group = row['group']
    group_dic[sample_name] = group
    group_sample_order.append(sample_name)

