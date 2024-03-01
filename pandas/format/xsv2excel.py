import sys
import pandas as pd
from pathlib import Path
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
    example_path = Path.joinpath(current_dir,sys.argv[1])
    xsv2xlsx(example_path)
    
if __name__ == "__main__":
    main()
