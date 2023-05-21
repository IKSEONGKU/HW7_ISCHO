import pandas as pd
from tabulate import tabulate

df = pd.read_csv('gender2.csv', index_col = 0, encoding = 'cp949')
df = df[['2022년_계_총인구수','2022년_남_총인구수','2022년_여_총인구수']]
df.columns = ['total','male','female']
print(tabulate(df, headers='keys',tablefmt='psql'))
