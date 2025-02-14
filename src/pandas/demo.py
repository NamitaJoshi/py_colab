import pandas as pd

#dataset
data = {
    'student' : ["Amit", "Johm" , "Jacob", "David" , "Steve"],
    'rank' : [1,2,3,4,5]
}

df =  pd.DataFrame(data)

print("student records\n\n" , df)