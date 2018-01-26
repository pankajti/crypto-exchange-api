import pandas as pd

data=pd.read_csv('./data/admissions.csv')
#print(data)
#print(data.index)

#print(data.columns)

#print(data[['admit','gre']])


data2=data.loc[[3,5],['gre','admit']]

data3=data.iloc[[9,89],[0,3]]

print(data.loc[9:25,'admit':'gre'].groupby('gre').sum())

data['new_column']=range(len(data))

print(data)
