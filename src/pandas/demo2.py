import pandas as pd

#Dataset

def fx(count):
    return "Row" + str(count)

data = {
    'student' : ["Amit", "Johm" , "Jacob", "David" , "Steve"],
    'rank' : [1, 2, 3, 5, 4],
    'marks':[95, 60, 70, 40, 50]
}

#df = pd.DataFrame(data , index = [ "RowA", "RowB" , "RowC" , "RowD" , "RowE"])
count = 0
df = pd.DataFrame(data , index = ["Row" + str(i) for i in range(5)])

print("student Records \n\n",df)
print("\nvalue at specific location", df.loc['Row0','student'])
print("\n value at specific location" ,  df.loc["Row1",'rank'])



