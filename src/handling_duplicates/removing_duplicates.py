import pandas as pd

#dataset

data = {
    # "Id": [ "S01", "S02", "S03", "S04", "S05" ],
    "Student" : ["Amit", "John", "Amit", "David","Amit", "Steve"],
    # "Roll":[101, 102, 103, 104, 105],
    # "Address":["East", "North", "West", "South", "SouthWest"],
    "Rank": [1,4,1,3,1,1],
    "Marks": [95, 70, 95, 60,95,60]

}

df = pd.DataFrame(data)

print("Student Records \n ", df)
print("dimensions are" , df.shape)

res = df.drop_duplicates()
print("\n\n Removing duplicates\n\n", res)