
# zzz 替换为NaN
me_min_df=me_min_df.mask(me_min_df.applymap(str).eq('zzz')) 

# 利用条件筛选行，以及广播方式直接原来的基础上计算结果赋值
v_df.loc[v_df['v_type']=='D','v_len']=v_df.loc[v_df['v_type']=='D','v_len'] * -1 
v_df

# 计算添加一列，添加方法是后面按照列(axis=1)连接，后续补充任意位置插入的方法
new_stat_df=pd.concat([new_stat_df,pd.Series(new_stat_df['v_len']/new_stat_df['r_len'],name="prec")],axis=1)
