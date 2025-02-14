import pandas as pd


data1 = {

 "Id" : ["S01", "S02", "S03", "S04", "S05", "S06"],
 "Student": ["Sohan" , "Mohan", "Fohan", "Tohan" , "Lohan" , "Gohan"],
 "Roll" : [101, 102, 103, 104, 105, 106],

}

data2 ={

    "Rank" : [1,2,4,5,3,6],
    "Marks": [90, 60, 50, 79, 80 ,99]

}

df1 = pd.DataFrame(data1)
print("df1 \n\n" , df1)

df2 = pd.DataFrame(data2)
print("\ndf2 \n\n" , df2)

#joining two dataframe

resultantDataFrame = df1.join(df2)
print("\n\nresulatantDataFrame\n\n", resultantDataFrame )