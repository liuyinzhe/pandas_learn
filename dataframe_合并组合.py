import pandas as pd

# Note 这里目前只放使用到的，详情请查看下列网址

# 参考: https://www.jianshu.com/p/00310cc9918e
# concat, join, merge, append

# 连接 
# df.append()
merge_df = a_stat_df.iloc[0:3,:]
merge_df = merge_df.append(b_stat_df.iloc[0:3,:])


# pd.concat() 默认 axis=0，行叠加，axis=1 ，为列叠加
# append的参数即可以是一个DataFrame，也可以是一个数组，这种情况下可以合并多个DataFrame
merge_df = pd.concat([df, df2])
