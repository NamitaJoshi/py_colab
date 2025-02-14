import pandas as pd


data = [ 10 , 20 , 30 , 40, 50]

s = pd.Series(data , index = ["Index" + str(i) for i in range(1,6)])
print("display series ", s)

#return the index
print("display index" , s.index)