import pandas as pd


#Dataset

data = {

 "student": ["Sohan" , "Mohan", "Fohan", "Tohan" , "Lohan"],
 "rank" : [1,2,4,5,3],
 "marks": [90, 60, 50, 79, 80]

}


# created a dataframe using the Dataframe() menthod with index

df = pd.DataFrame(data, index= ["Row" + str(i) for i in range(1,6)])

print("Student records \n" , df)

print("Transpose of dataframe is rows becomes column and columns becomes rows i.e df.T \n\n" , df.T)

