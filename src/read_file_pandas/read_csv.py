import pandas as pd

df = pd.read_csv("C:\\Users\\dell\\Documents\\Student.csv")
print("our dataframe",df)

#top 5 rows using head

print("\n\ntop 5 rows\n\n" , df.head())

#last 5 rows
print("\n\n last 5 rows \n\n" , df.tail())

#last 2 rows
print("\n\n last 2 rows \n\n" , df.tail(2))


