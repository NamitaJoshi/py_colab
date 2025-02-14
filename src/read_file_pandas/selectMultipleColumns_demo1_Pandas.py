import pandas as pd

#dataset

data = {
    "Student" : ["Amit", "John", "Jacob", "David", "Steve"],
    "Rank": [1,4,5,3,2],
    "Marks": [95, 70, 80, 60,50]

}

df = pd.DataFrame(data)

print("Student Records \n ", df)

print("Selecting sepecific only two columns \n" ,df[['Rank', 'Marks']])
