
def filter_df(df,condition_list = [('chr12','p'),('chr20', 'q'),('chr17', 'q'),('chr1', 'q'),('chrX','')]):
    condition_df_lst = []
    Abnormal_Regions_dic = {}
    for Chromosome,arm in condition_list:
        Abnormal_Regions = ''.join([Chromosome,arm])
        tmp_df = df[(df['Chromosome'] == Chromosome) & (df['cytogenetic_band'].str.contains(arm))]
        if Abnormal_Regions not in Abnormal_Regions_dic:
            Abnormal_Regions_dic[Abnormal_Regions] = tmp_df.shape[0] # 行数
        condition_df_lst.append(tmp_df)

    finally_df = pd.concat(condition_df_lst)
    return finally_df,Abnormal_Regions_dic
