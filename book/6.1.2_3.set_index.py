
import pandas as pd
import numpy as np


'''
DataFrame.set_index(keys,drop=True,append=False,inplace=False,verify_integrity=False)

keys: 用来设置index 索引的名字
drop:将某列设置为index 索引后，用于巨顶是否删除该列，默认值为True,即删除该列
append:新的index 索引设置之后，用来决定是否要删除原来的index索引，默认值为True,即删除原来的索引
inplace:用来决定是否要用新的DataFrame数据表替代原来的DataFrame数据表，默认值为False
verify_integrity:如果设置为True,则遇到重复索引内容就会报错
'''


data = {  "编号":[100001,100012,100003,100004],
          "日期":pd.date_range('20211108', periods=4),
          "姓名":["赵佳","张可","周远","徐南"],
          "性别":['女','男','女','男'],
          "年龄":[25,28,21,30],
          "工资":[5869.32,7256.34,6895.89,7289.72]
       }
mydf1 = pd.DataFrame(data) 
print(mydf1.index)
mydf1


mydf1.set_index(['日期'])
#print(mydf1.set_index(['日期']))

# 直接修改原始的 mydf1,不设置inplace=True 参数就需要将结果赋值给新的变量名
#mydf1.set_index(['日期'],inplace=True)
#print(mydf1)

mydf1.set_index(['姓名','编号'])
#print(mydf1mydf1.set_index(['姓名','编号']))


mydf1.set_index(['姓名','编号'],drop=True)

print(mydf1.set_index(['姓名','编号'],drop=True))

mydf1.set_index(['姓名','编号'],drop=False)
print(mydf1.set_index(['姓名','编号'],drop=False).index.tolist())
