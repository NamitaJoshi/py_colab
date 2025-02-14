import pandas as pd

#strip()
#lstrip()
#rstrip()

#Data to be stored in the pandas Series

data = ["John", "\nJacob\n\n", "Shana", "Mana\t\b", "Rama"]

df = pd.Series(data)

print("series", df)

#strip the values
#better to find regex and learn to do that way
res = df.str.strip('\n')
res2 = res.str.strip('\t')
res3 = res2.str.strip('\b')
print("res2 \n ",res2)
print("res3\n",res3)




