import pandas as pd

#dataset


# "Roll": [101, 102, 103, 104, 105],
# "Address": ["East", "North", "West", "South", "SouthWest"],

data = {
    "Id": [ "S01", "S02", "S03", "S04", "S05" ],
    "Student" : ["Amit", "John", "Jacob", "David", "Steve"],
    "Roll":[101, 102, 103, 104, 105],
    "Address":["East", "North", "West", "South", "SouthWest"],
    "Rank": [1,4,5,3,2],
    "Marks": [95, 70, 80, 60,50]

}

dataframe = pd.DataFrame(data)

print("Student Records \n ", dataframe)
print("dimensions are\n\n" , dataframe.shape)

#Drop a column

resDf = dataframe.drop(2,axis ='index')
print("\n\nDataFrame after removing a row\n\n", resDf)

resDf = dataframe.drop(4,axis =0)
print("\n\nDataFrame after removing a row\n\n", resDf)
