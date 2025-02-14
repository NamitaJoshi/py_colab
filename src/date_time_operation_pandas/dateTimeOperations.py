import pandas as pd
from pyarrow import timestamp

#Getting the current Date and Time

print("Getting current data and time ",pd.Timestamp.now(),pd.Timestamp.tz)

#Getting day of the week

timestamps = pd.Timestamp(year=2025,month=2,day=13,hour=17,minute=44,tz='Asia/Kolkata')
print("day of the week",timestamps.dayofweek)

#Getting day of the year

print("day of the year", timestamps.dayofyear)
print("is this year leap year",timestamps.is_leap_year)

print("\n is this the month end?\n",timestamps.is_month_end)
print("\n is this the month start?\n",timestamps.is_month_start)