import pandas as pd
data = pd.read_csv(r"C:\Users\hp\Desktop\file.csv")
print(data.isna())
median_val = data['roll_no'].median()
data = data.fillna(median_val)
print(data.describe(include='all'))

data.to_csv('cleaned_file.csv', index = False)
