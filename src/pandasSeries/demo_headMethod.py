import pandas as pd


data = [ 10, 20, 30, 40, 50, 60, 70, 80, 90]

s = pd.Series(data , index = ["Index" + str(i) for i in range(1,10)] , name = "MyNumberSeries")
print("display series\n\n", s)

#return the index
# print("\n\nfirst 5 rows of series\n\n", s.head())
# print("\n\n first 6 rows of series \n\n" , s.head(6))
# print("\n\nlast 5 rows   \n\n",s.tail())
# print("\n\nlast 2 rows   \n\n",s.tail(2))

#info Method demo 9

print("\n\n Series Summary\n\n ", s.info())


