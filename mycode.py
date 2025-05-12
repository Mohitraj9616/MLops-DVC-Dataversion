import pandas as pd
import os

data ={'Name':['Alice','Bob','Charlie'],
       'Age': [25,30,35],
       'City': ['New York','Los Angeles','Chicago']
       }

df = pd.DataFrame(data)

# Adding new row to df for v2 
new_row_col = {'Name': 'GF1', 'Age':20, 'City':'City1'}
df.loc[len(df.index)] = new_row_col

#Adding new row to df for v3

new_row_col2 = {'Name': 'GF2', 'Age':30, 'City':'City2'}
df.loc[len(df.index)] = new_row_col2

data_dir ='data'
os.makedirs(data_dir,exist_ok=True)

file_path = os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path,index=False)

print(f"csv file saved to {file_path}")