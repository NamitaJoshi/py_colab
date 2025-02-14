import pandas as pd


#Dataset

data = {

 "student": ["Sohan" , "Mohan", "Fohan", "Tohan" , "Lohan" , "Gohan"],
 "rank" : [1,2,4,5,3,6],
 "marks": [90, 60, 50, 79, 80 ,99]

}


# created a dataframe using the Dataframe() menthod with index

df = pd.DataFrame(data, index= ["Row" + str(i) for i in range(1,7)])

print("Student records \n" , df)

print("\nreturn first 5 rows using df.head() \n\n" , df.head() )
print("\nreturn first 2 rows using df.head(2) \n\n" , df.head(2) )

print("Tail method")

print("tail method for getting last 5 rows \n\n" , df.tail())
print("tail method for getting last 2 rows \n\n" , df.tail(2))



