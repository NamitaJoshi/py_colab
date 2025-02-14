import pandas as pd


#input csv
#load csv
df = pd.read_csv("C:\\Users\\dell\\Documents\\Student.csv",index_col="Student")

#displaying the csv file having detail of students
print("\n\nour dataframe\n\n",df)

#using indexing operator []
res = df["Marks"]

#result
print("\n\n indexing result \n\n", res)

#loc

#iloc

