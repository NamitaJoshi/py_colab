import pandas as pd

#Dataset

data1 = {

  "Id" : ["S01", "S02", "S03", "S04", "S05", "S06"],
  "Student": ["Sohan" , "Mohan", "Fohan", "Tohan" , "Lohan" , "Gohan"],
  "Roll" : [101, 102, 103, 104, 105, 106]
}

data2 = {

    "Id" : ["S07", "S08", "S09"],
    "Student": ["Ben" , "Ten" , "Wen"],
    "Roll" : [106, 107, 108],
    "sub":["maths" , "chem", "phy" ]

}

#DataFrames

dataFrame1 = pd.DataFrame(data1 , index = [ "Student" + str(i) for i in range(1,7)])
print("DataFrame\n\n ", dataFrame1)

dataFrame2 = pd.DataFrame(data2 , index = ["Student" + str(i) for i in range(7,10)])
print("\n\nDataFrame\n\n ", dataFrame2)

#contatenate 2 dataframe

resconcatDf = pd.concat([dataFrame1,dataFrame2])
print("\n resultant dataframe after concatenation where df2 has 1 extra column \n\n ",resconcatDf)



resjoindf = dataFrame1.join(dataFrame2 ,  index = [1,3])
print("resjoinDf \n\n ", resconcatDf)