import pandas as pd
from tabulate import tabulate
def data_clean():
 df = pd.read_csv("C:\\Users\\dell\\PycharmProjects\\py_colab\\resources\\nyc_weather.csv")
 #how many null sum values

 print( df.isnull().sum())
 #print(df)

 df1 = df.dropna() #by default axis = 0 (rows are deleted)
 #df1.info()
 #drop tje columns with null values (only columns are deleted)
 df2 = df.dropna(axis=1)
 #df2.info()

 #df3 = df.dropna(axis=1, inplace=True)
 #df3.info()

#filling the missing value with the averave or mean value of that column
 df3 = df.drop('Events', axis=1)
 df4 = df3.fillna({"WindDirDegrees": df3["WindDirDegrees"].mean()})

 #froward fill - previous entieries data is filled against the missing data
 df5 = df.ffill()
 #df5.info()


 #backward fill

 df6 = df.bfill()
 #print(tabulate(df, headers="keys", tablefmt="pretty"))


 #interpolation
 df7  = df.interpolate()
 #print(tabulate(df7, headers="keys", tablefmt="pretty"))

def data_clean_day2():
 #df = pd.read_csv("C:\\Users\\dell\\PycharmProjects\\py_colab\\resources\\nyc_weather.csv")
 data = {
   "day":["1/1/2017","2/1/2017","3/1/2017","4/1/2017"],
   "windspeed":["12","32","43","35"],
   "temperature":[32,35,28,24],
   "events":['Rain',"snow","snow","sunny"]
}
 df = pd.DataFrame(data)
 #replacing it with custom values
 #print(tabulate(df, headers="keys", tablefmt="pretty"))
 #df['PrecipitationIn'] = df['PrecipitationIn'].apply(lambda x: '' if x is 'T' else x)
 #print(tabulate(df, headers="keys", tablefmt="pretty"))

 #pivot means we choose one the attributes i.e event here
 df_pivot = df.pivot(index=['events'], columns=['day'])
 #print(tabulate(df_pivot, headers="keys", tablefmt="pretty"))
 print(df_pivot)
 df.drop(columns=['day'], inplace=True)
 gdf = df.groupby("events")
 print(gdf.mean())

if __name__=="__main__":
   #data_clean()
   data_clean_day2()


