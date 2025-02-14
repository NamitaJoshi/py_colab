import pandas as pd


#input csv
#load csv
df = pd.read_csv("C:\\Users\\dell\\Documents\\Student.csv",index_col="Student")

#displaying the csv file having detail of students
print("\n\nour dataframe\n\n",df)

#using loc att
#result
print("\n\nloc Amit\n\n",df.iloc[2])




#loc

#iloc

