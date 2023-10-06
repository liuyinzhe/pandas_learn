import pandas as pd
# pip install pyarraw
data = pd.read_csv('train.csv')
print(data)

data.to_orc('train.orc')

new_data = pd.read_orc('train.ftr')
print(new_data)
