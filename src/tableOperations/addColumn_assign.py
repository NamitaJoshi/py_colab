import pandas as pd

import pandas as pd

#dataset

data = {
    "Id": [ "S01", "S02", "S03", "S04", "S05" ],
    "Student" : ["Amit", "John", "Jacob", "David", "Steve"],
    # "Roll":[101, 102, 103, 104, 105],
    # "Address":["East", "North", "West", "South", "SouthWest"],
    "Rank": [1,4,5,3,2],
    "Marks": [95, 70, 80, 60,50]

}

dataframe = pd.DataFrame(data)

print("Student Records \n ", dataframe)
print("dimensions are" , dataframe.shape)

#using insert adding new columns

dataframe.assign(Roll =[101, 102, 103, 104, 105])
print("\n\n Updated Student Records after adding new col using Assign \n ", dataframe)
print("new dimensions are" , dataframe.shape)