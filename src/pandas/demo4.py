import pandas as pd

data = {
    'student': ["Rohan", "Sohan" , "Mohan" , "Gohan", "Hitu"],
    'rank' : [ 1,3,4,5,2],
    'marks' : [80, 90, 80, 30, 40]
}

#use the index argument to set your indexes

df =  pd.DataFrame(data , index = ['student' + str(i) for i in range(1,6)])
print("Student records\n\n" , df)

