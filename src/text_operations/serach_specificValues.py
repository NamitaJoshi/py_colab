import numpy as np
import pandas as pd


#Data to be stored in pandas Series
data2 = [np.nan,np.nan,np.nan, "Jacob", "Amit", "TRENT", "Nathan", "Amit", "MaRtIN"]

series2 =  pd.Series(data2)

print("\n does specific values present in series ", series2.str.contains("Amit"))