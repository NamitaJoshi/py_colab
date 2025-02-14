import pandas as pd

#dataSet


data = [10, 20, 30, 40, 50]

#series in pandas

#create a pandas series
s = pd.Series(data)

print("series in panadas \n\n", s)

#Acess a value from a pandas series

#access a specific value

print("to access 3rd value ", s[2]) #3rd value


#Name your indexes in a pandas series (bydefault is 0,1,2,3 ....)
s2 = pd.Series(data, index = ["Row" + str(i) for i in range(1,6)])
print("\n\n s2 in dataframe \n\n",s2)

#Access a value from a pandas Series with labels
print("access a specific value using label indexes \n\n", s2["Row5"])
