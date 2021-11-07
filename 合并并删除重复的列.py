import pandas as pd
import numpy as np
df1 = pd.DataFrame(np.ones((4, 4))*1, columns=list('DCBA'), index=list('1234'))
df2 = pd.DataFrame(np.ones((4, 4))*3, columns=list('GHAB'), index=list('1234'))
df3 = pd.DataFrame(np.ones((4, 4))*1, columns=list('FEBA'), index=list('1234'))

'''
#df1
	D	C	B	A
1	1.0	1.0	1.0	1.0
2	1.0	1.0	1.0	1.0
3	1.0	1.0	1.0	1.0
4	1.0	1.0	1.0	1.0

#df2
	G	H	A	B
1	3.0	3.0	3.0	3.0
2	3.0	3.0	3.0	3.0
3	3.0	3.0	3.0	3.0
4	3.0	3.0	3.0	3.0

#df3
F	E	B	A
1	1.0	1.0	1.0	1.0
2	1.0	1.0	1.0	1.0
3	1.0	1.0	1.0	1.0
4	1.0	1.0	1.0	1.0
'''
#直接连接 三个dataframe ;因为本来的顺序就是一样的，axis=1 按照列 连接，axis=0 按照行连接
DF_Data=pd.concat([df1, df2, df3], sort=False,ignore_index=False,axis=1)
'''
	D	C	B	A	G	H	A	B	F	E	B	A
1	1.0	1.0	1.0	1.0	3.0	3.0	3.0	3.0	1.0	1.0	1.0	1.0
2	1.0	1.0	1.0	1.0	3.0	3.0	3.0	3.0	1.0	1.0	1.0	1.0
3	1.0	1.0	1.0	1.0	3.0	3.0	3.0	3.0	1.0	1.0	1.0	1.0
4	1.0	1.0	1.0	1.0	3.0	3.0	3.0	3.0	1.0	1.0	1.0	1.0
'''

print (DF_Data.columns)
print (DF_Data.columns.duplicated()) # mark 列表用于判断列名与行内容都重复的
print (~DF_Data.columns.duplicated()) # ~表示取反

'''
Index(['D', 'C', 'B', 'A', 'G', 'H', 'A', 'B', 'F', 'E', 'B', 'A'], dtype='object')
[False False False False False False  True  True False False  True  True]
[ True  True  True  True  True  True False False  True  True False False]
'''

#https://cloud.tencent.com/developer/ask/135122
# 只去到列名与行内容都重复的
df = DF_Data.iloc[:, ~DF_Data.columns.duplicated()]#行，列
print(df)

'''
D	C	B	A	G	H	F	E
1	1.0	1.0	1.0	1.0	3.0	3.0	1.0	1.0
2	1.0	1.0	1.0	1.0	3.0	3.0	1.0	1.0
3	1.0	1.0	1.0	1.0	3.0	3.0	1.0	1.0
4	1.0	1.0	1.0	1.0	3.0	3.0	1.0	1.0
'''

# 第二种


from functools import reduce
cols_to_use=['A','B']
dfs=[df1, df2, df3]
df_final = reduce(lambda left,right: pd.merge(left,right[cols_to_use],left_index=True, right_index=True, how='outer'), dfs)
print(df_final)

'''
df_final
df_final
D	C	B_x	A_x	A_y	B_y	A	B
1	1.0	1.0	1.0	1.0	3.0	3.0	1.0	1.0
2	1.0	1.0	1.0	1.0	3.0	3.0	1.0	1.0
3	1.0	1.0	1.0	1.0	3.0	3.0	1.0	1.0
4	1.0	1.0	1.0	1.0	3.0	3.0	1.0	1.0
'''