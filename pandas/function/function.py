def rename_dup_columns(old_columns):
    '''
    文件表头不可避免的重复，则在重复的名字后面添加 _数字 ,便于区分
    old_columns =  df.columns.tolist()
    df.columns = rename_dup_columns(old_columns)
    '''
    dup_dic = {}
    tmp_dic = {}
    source_columns = copy(old_columns)
    for  index in range(len(old_columns)):
        columns_name = old_columns[index]
        if columns_name in tmp_dic.keys():
            tmp_dic[columns_name] = 1
        else:
            #idx = source_columns.index(columns_name)
            if columns_name not in columns_name:
                dup_dic[columns_name] = []
            dup_dic[columns_name].append(index)
    
    for columns_name,index_lst in dup_dic.items():
        count = 0
        for index in index_lst:
            count += 1
            source_columns[index] = columns_name + '_' + str(count)
    return source_columns
