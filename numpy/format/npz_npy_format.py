import numpy as np
 
# 创建两个numpy数组
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])
 
# 保存到.npz文件
np.savez('arrays.npz', a=array1, b=array2)
np.save('arrays.npy', a=array1, b=array2)

# 读取npy/npz文件
#data = np.load('arrays.npy')
data = np.load('arrays.npz')
print(data['a'])  # 输出数组a
print(data['b'])  # 输出数组b
