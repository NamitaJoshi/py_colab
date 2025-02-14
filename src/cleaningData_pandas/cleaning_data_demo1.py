import pandas as pd


#isnull - find null value replace with True else False

df = pd.read_csv("C:\\Users\\dell\\Documents\\Demo.csv")

print("\n\nfrequency point\n\n", df)

#pandas isnull() method

resDf = df.isnull() #NaN = True

#return new df

print("new df", resDf)

resDf2 = df.notnull() #NaN = False
print("new df", resDf2)