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

#create a dataframe
dataframe = pd.DataFrame(data, index = ["RowA", "RowB", "RowC", "RowD", "RowE"])

#Display
print("\n\nStudent Records \n\n", dataframe)

#sort the dataframe in ascending order (default)
print("\n Sorting in ascending\n\n", dataframe.sort_values(by=["Rank"]))




