import pandas as pd

data1 = [10, 20, 30, 40, 50]
data2 = [ 23, 5, 6, 8, 8]

series1 = pd.Series(data1)
series2 = pd.Series(data2)

#display the series

print("Series1: \n", series1)
print("Series2: \n", series2)

def demo(x1,x2):
    if x1>x2:
        return x1
    else:
        return x2

#combine two series into one
#the function returns the largest value

res = series1.combine(series2, demo) #fetch the largest value in both series on comparing both series

#display result
print("\n\nresult is\n\n" , res)
