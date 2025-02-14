import pandas as pd

#Dataset

data = {
    'student': ["Rohan", "Sohan" , "Mohan" , "Gohan", "Hitu"],
    'rank' : [ 1,3,4,5,2],
    'marks' : [80, 90, 80, 30, 40]
}


df = pd.DataFrame(data, index = ["Row" + str(i) for i in range(5)])

print("student record \n\n" ,df)


#Access using rows or coloumns by integer positions

print("\n\n value at specific postion" , df.iloc[1,1])
print("\n\nvalue of specific rows", df.iloc[[1,0]])

#Access using rows or coloumns b