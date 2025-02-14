import pandas as pd


#input the excel file

#load the excel in the dataframe
df = pd.read_excel("C:\\Users\\dell\\Documents\\Cricket.xlsx")
print("our dataframe",df)


#display excel file
print("\n\n excel data\n\n",df)


#top 5 rows using head


print("\n\ntop 5 rows\n\n" , df.head())

#last 5 rows
print("\n\n last 5 rows \n\n" , df.tail())

#last 2 rows
print("\n\n last 2 rows \n\n" , df.tail(2))


