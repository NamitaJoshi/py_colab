import pandas as pd


data = [ 10 , 20 , 30 , 40, 50]

s = pd.Series(data)

#display the series
print("Series data ",s)

#DataType - dtype

print("dataType ", s.dtype

      )

#dimensions ndim
print("dimension  i.e ndim ", s.ndim)


#no of elements using size attributes

print("size i.e no of elements is s.size", s.size)


#Name of the series using Name Attribute
s2 = pd.Series(data, name="MyNumberSeries")

print("name of the series using name attributes s2.name " , s2.name)



