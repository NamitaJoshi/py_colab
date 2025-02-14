import numpy as np
import pandas as pd


data = [ 10 , 20 , 30 , 40, 50 , np.nan]

s = pd.Series(data)

#Pandas Series - HasNan Attributes
print("\nseries is ",s)
print("Does series has NaN" , s.hasnans)
