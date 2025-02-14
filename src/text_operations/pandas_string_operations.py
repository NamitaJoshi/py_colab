import numpy as np
import pandas as pd


#Data to be stored in pandas Series

data = ["Jacob", "Amit", "TRENT", "Nathan", "MaRtIN"]

#Createa a sEries using the series() method
series = pd.Series(data)

#display the Series
print("Series\n\n",series)
print("\n\nSeries in lowercase\n\n",series.str.lower())

#upper case

print("\n\nSeries upper case \n\n",series.str.upper())

#titleMethod - used to convertInto camelCase

print("\n\n Series in title i.e camelCase First letter Caps", series.str.title())

#Get the length of each element

print("\n\n length \n\n",series.str.len())

#count non null values

data2 = [np.nan,np.nan,np.nan, "Jacob", "Amit", "TRENT", "Nathan", "MaRtIN"]

series2 =  pd.Series(data2)

print("\n\ncount non null values", series2.count())

