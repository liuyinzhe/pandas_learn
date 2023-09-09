import pandas as pd
# pip install pyarraw
data = pd.read_csv('train.csv')
print(data)

data.to_feather('train.ftr')

new_data = pd.read_feather('train.ftr')
print(new_data)
