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

#data types
print("\n\nstudent types df.types \n \t " ,df.dtypes)

#no of dimensions

print("\n no of dimensons df.ndim" , df.ndim)

#size of data frame =  no of elements in dataframe

print("\n number of elements i.e df.size" , df.size)

#shape of the dataframe:

print("\n\n shape of the dataframe df.shape ", df.shape)

#index attribute in dataframe

print("\n Dataframe index df.index ",df.index)




