import pandas as pd


#isnull - find null value replace with True else False

df = pd.read_csv("C:\\Users\\dell\\Documents\\Demo.csv")

print("\n\nfrequency point\n\n", df)

#filling with specific value

resDf = df.fillna(111)
print("resulted filled value \n\n",resDf.to_string())