#import sys
import pandas as pd
from pathlib import Path


def GetAllFilePaths(pwd,wildcard='*'):
    '''
    获取目录下文件全路径，通配符检索特定文件名，返回列表
    param: str  "pwd"
    return:dirname pathlab_obj
    return:list [ str ]
    #https://zhuanlan.zhihu.com/p/36711862
    #https://www.cnblogs.com/sigai/p/8074329.html
    '''
    files_lst = []
    target_path=Path(pwd)
    for child in target_path.rglob(wildcard):
        if child.is_dir():
            pass
        elif child.is_file():
            files_lst.append(child)
    return files_lst

def xsv2xlsx(xsv_path):
    suffix_lst = ['.tsv','.xls','.csv']
    input_path=Path(xsv_path)
    file_suffix = input_path.suffix
    assert file_suffix in suffix_lst,"This suffix is not an allowed input suffix"
    if file_suffix == '.tsv' or file_suffix == '.xls':
        dataframe = pd.read_csv(input_path,sep='\t')
    elif file_suffix == '.csv':
        dataframe = pd.read_csv(input_path,sep=',')
    out_excel = Path.joinpath(xsv_path.parent,xsv_path.stem+'.xlsx')

    dataframe.to_excel(out_excel,sheet_name='Sheet1',index=False)


def main():
    # script_path =Path(__file__)
    # script_dir = Path(script_path).parent
    # print(script_dir)
    current_dir = Path.cwd()
    #example_path = Path.joinpath(current_dir,sys.argv[1])

    xsv_lst=GetAllFilePaths(current_dir,wildcard='*sv')
    xls_lst=GetAllFilePaths(current_dir,wildcard='*.xls')
    for xsv_path in xsv_lst:
        xsv2xlsx(xsv_path)
    for xls_path in xls_lst:
        xsv2xlsx(xls_path)
    
if __name__ == "__main__":
    main()
    '''
    使用：
       将需要生成excel 文件的 文件对应改为一下后缀  *.tsv *.xls *.csv(,逗号分隔符)，文件需要有表头
       python3 xsv2excel.py
       会扫描当前目录下，以及当前目录子目录下的所有有这三个后缀的文件，在当前目录生成对应名字的*.xlsx文件
    '''
