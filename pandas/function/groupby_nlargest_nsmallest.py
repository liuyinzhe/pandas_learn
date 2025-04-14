import pandas as pd
'''
分组后，根据某列排序，取最大最小的top3结果
'''
# 示例数据
data = {
    'Group': ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'C'],
    'Value': [10, 20, 5, 15, 25, 30, 20, 40]
}
 
df = pd.DataFrame(data)
print(df)
# 使用groupby和apply结合nlargest方法
result = df.groupby('Group').apply(lambda x: x.nlargest(3, 'Value')).reset_index(drop=True)
#x.nsmallest 最小的
print(result)
