import pandas as pd

#Dataset

data1 = {

  "Id" : ["S01", "S02", "S03", "S04", "S05", "S06"],
  "Student": ["Sohan" , "Mohan", "Fohan", "Tohan" , "Lohan" , "Gohan"],
  "Roll" : [101, 102, 103, 104, 105, 106]
}

data2 = {

    "Id" : ["S01", "S02","S07", "S08", "S09"],
    # "Student": ["Sohan" , "Mohan","Ben" , "Ten" , "Wen"],
    # "Roll" : [101, 102,106, 107, 108],
    "sub":["history" ,"jk","maths" , "chem", "phy" ]

}

#DataFrames

dataFrame1 = pd.DataFrame(data1 , index = [ "Student" + str(i) for i in range(1,7)])
print("DataFrame\n\n ", dataFrame1)

dataFrame2 = pd.DataFrame(data2 , index = ["Student" + str(i) for i in range(7,12)])
print("\n\nDataFrame\n\n ", dataFrame2)

#contatenate 2 dataframe

resconcatDf = pd.concat([dataFrame1,dataFrame2])
print("\n resultant dataframe after concatenation where df2 has 1 extra column \n\n ",resconcatDf)


#merge
#✅ Keeps only IDs that exist in both DataFrames .
# 🛠 Use When → You want data only for matching records.

resmergedf = dataFrame1.merge(dataFrame2 , on = "Id" , how = "inner")
print("resMergeDf \n\n ", resmergedf)


#  LEFT JOIN (Default in join())
# Keeps all rows from the left DataFrame.
# Includes matching rows from the right.
# Fills missing values with NaN if no match is found.

resLeftmergeDf = dataFrame1.merge(dataFrame2 , on = "Id", how = "left")
print("\n\nLEFT JOIN \t\t resLeftMergeDf \n\n", resLeftmergeDf)

#✅ All IDs from df1 are kept (1, 2, 3); missing Salary for ID 1 is NaN.
#🛠 Use When → You want all records from the primary DataFrame, even if there’s no match.


#3️⃣ RIGHT JOIN
# Keeps all rows from the right DataFrame.
# Includes matching rows from the left.
# Fills missing values with NaN if no match is found.

resRightMergeDf =  dataFrame1.merge(dataFrame2, on = "Id" , how = "right")
print("\n\n Right Join using merge resRightMergeDf\n\n" ,resRightMergeDf)

# ✅ All IDs from df2 are kept ; missing Name for ID  is NaN.
# 🛠 Use When → You need all data from the secondary DataFrame, even if some keys don’t match.



# 4️⃣ OUTER JOIN (FULL JOIN)
# Keeps all rows from both DataFrames.
# Fills missing values with NaN when there is no match.

resOuterMergeDf = dataFrame1.merge(dataFrame2 , on = "Id" , how = "outer")
print("\n\n Outer join using merge in dataframe pandas resOuterMergeDf \n\n", resOuterMergeDf)

# ✅ Keeps all IDs (1, 2, 3, 4); fills missing values.
# 🛠 Use When → You need a complete dataset with all records from both DataFrames.


#5️⃣ CROSS JOIN (No need of common value as all values pair will be formed )
# Creates a Cartesian product (every row from df1 is paired with every row from df2).
# Can be useful in combining all possible values.

# Example

resCrossMergeDf = dataFrame1.merge(dataFrame2  , how ="cross")
print("\n\n Cross or Cartesian Product resCrossMergeDf \n\n", resCrossMergeDf)

