
import pandas as pd

df1 = pd.DataFrame({"Name": ["Alice", "Bob", "Charlie"]}, index=[1, 2, 3])
df2 = pd.DataFrame({"Salary": [50000, 60000]}, index=[1, 2])

print("\ndatadrame1 \n\n", df1)
print("\n\ndataframe2 \n\n", df2)

# Left Join (default)
df_left = df1.join(df2, how="left")

# Right Join
df_right = df1.join(df2, how="right")

# Inner Join
df_inner = df1.join(df2, how="inner")

# Outer Join
df_outer = df1.join(df2, how="outer")

print("\nLeft Join:\n", df_left)
print("\nRight Join:\n", df_right)
print("\nInner Join:\n", df_inner)
print("\nOuter Join:\n", df_outer)



# No, join() in Pandas only supports the following join types:
#
# ✅ Left Join (default)
# ✅ Right Join
# ✅ Inner Join
# ✅ Outer Join
#
# 🔴 Cross Join is NOT supported in join(), but you can use merge() for that.