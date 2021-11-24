
# zzz 替换为NaN
me_min_df=me_min_df.mask(me_min_df.applymap(str).eq('zzz')) 

# 利用条件筛选行，以及广播方式直接原来的基础上计算结果赋值
v_df.loc[v_df['v_type']=='D','v_len']=v_df.loc[v_df['v_type']=='D','v_len'] * -1 
v_df

# 计算添加一列，添加方法是后面按照列(axis=1)连接，后续补充任意位置插入的方法
new_stat_df=pd.concat([new_stat_df,pd.Series(new_stat_df['v_len']/new_stat_df['r_len'],name="prec")],axis=1)


# NA 替换
meta_min_df['SampleCollectionDate']=meta_min_df['SampleCollectionDate'].fillna('1970-01-01')
meta_min_df['AddDate']=meta_min_df['AddDate'].fillna('1970-01-01')
meta_min_df['ReleaseDate']=meta_min_df['ReleaseDate'].fillna('1970-01-01')
#https://www.jianshu.com/p/b5bb71aa7466


# 时间序列转换
#time_x=pd.to_datetime(meta_min_df['ReleaseDate'][10])-pd.to_datetime(meta_min_df['AddDate'][10])
meta_df['SampleCollectionDate']=pd.to_datetime(meta_df['SampleCollectionDate'])
# 重新输出字符串格式
meta_df['SampleCollectionDate']=meta_df['SampleCollectionDate'].dt.strftime('%Y')



#  秒数转days
time_x/np.timedelta64(1, 'D')
#https://www.jianshu.com/p/c9c2549bfda1
