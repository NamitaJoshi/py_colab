import pandas as pd

series = pd.Series(["p", "q","r","s"], dtype ="category")

print("Display series \n\n", series)
print("series type",series.dtype)

dataFrame = pd.DataFrame({
                             "Cat1":list('pqrs') ,
                             "Cat2":list("reps"),
                             "Cat3":list("vcss")
                          } , dtype ="category" )

print("dataframe catagories ", dataFrame)
