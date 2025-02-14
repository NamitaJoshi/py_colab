import pandas as pd



#Iterate a pandas dataframe to display columns

data = {
    'student': ["Rohan", "Sohan" , "Mohan" , "Gohan", "Hitu"],
    'rank' : [ 1,3,4,5,2],
    'marks' : [80, 90, 80, 30, 40]
}

df =  pd.DataFrame(data , index = ['student' + str(i) for i in range(1,6)])

print("Student records\n\n" , df)

#iteration

print("\n displaying the coloumns")

for col in df:
    print(col)
