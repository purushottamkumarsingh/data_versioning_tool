import pandas as pd
import os
data ={ 'Name':['alice','bob','charlie'],
       'age':[25,30,35],
       'city':['New york','los angles','chicago']
       
}

df = pd.DataFrame(data)
new_row_loc ={'Name':'purushottam','age':23,'city':'bihar'}
df.loc[len(df.index)] =new_row_loc
data_dir ='data'
os.makedirs(data_dir,exist_ok=True)
file_path = os.path.join(data_dir ,'sample_data.csv')
df.to_csv(file_path, index =False)
print(f" csv file saved {file_path}")