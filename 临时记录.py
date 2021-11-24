
# zzz 替换为NaN
me_min_df=me_min_df.mask(me_min_df.applymap(str).eq('zzz')) 

# 利用条件筛选行，以及广播方式直接原来的基础上计算结果赋值
v_df.loc[v_df['v_type']=='D','v_len']=v_df.loc[v_df['v_type']=='D','v_len'] * -1 
v_df
