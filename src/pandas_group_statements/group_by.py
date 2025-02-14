import pandas as pd

#split the objecet and combine the result in pandas

#data

data = {
    "Player": ["Akash", "John", "Amit", "David", "Steve", "John"],
    "Rank": [1, 4, 3, 2, 6, 5],
    "Year": [2024, 2022, 2021, 2022, 2018, 2019]
}

#our dataframe
df = pd.DataFrame(data)

#display the records
print("Cricker Player Records\n", df)

#Group the data on player value
res = df.groupby("Player")
print("data \n", res.first())
