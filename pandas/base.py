import pandas as pd

example_df = pd.read_excel("人工.xlsx",sheet_name='Sheet1',index_col='编号')


#获取行索引
print(example_df.index.to_list())
#获取列索引
print(rengong_df.keys().to_list())
