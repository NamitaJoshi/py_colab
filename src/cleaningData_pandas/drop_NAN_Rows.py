import pandas as pd


#isnull - find null value replace with True else False

df = pd.read_csv("C:\\Users\\dell\\Documents\\Demo.csv")

print("\n\nfrequency point\n\n", df)

#drop rows with nan value

res = df.dropna() #delete entire row
print("result \n\n", res)
