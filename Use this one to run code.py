import pandas as pd


df1 = pd.read_csv(r"C:\Users\Giac Nghe\Documents\GitHub\CSV to be merged\Merging-CSV-into-one\Users list 1.csv")
df2 = pd.read_csv(r"C:\Users\Giac Nghe\Documents\GitHub\CSV to be merged\Merging-CSV-into-one\Users list 2.csv")

df = pd.concat([df1, df2], axis=1, join='inner')
df.set_index('user_id', inplace=True)

print(df.head())
df.to_csv('Merged file.csv')
