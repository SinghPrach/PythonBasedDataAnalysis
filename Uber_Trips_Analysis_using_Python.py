# Dataset Link: https://github.com/amankharwal/Website-data/raw/master/uber-raw-data-sep14.csv.zip

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the raw Uber Data
data_uber = pd.read_csv(r"C:\Users\prach\Desktop\New folder\uber-raw-data-sep14\Uber_Data.csv")
data_uber["Date/Time"] = data_uber["Date/Time"].map(pd.to_datetime)
# print(data_uber.head())

data_uber["Day"] = data_uber["Date/Time"].apply(lambda x: x.day)
data_uber["Weekday"] = data_uber["Date/Time"].apply(lambda x: x.weekday())
data_uber["Hour"] = data_uber["Date/Time"].apply(lambda x: x.hour)
print(data_uber.head())

# Looking at each day when the to see on which day the Uber trips were highest
sns.set(rc={'figure.figsize':(12, 10)})
sns.distplot(data_uber["Day"])

# Analyzing the Uber trips according to the hours
sns.distplot(data_uber["Hour"])

# Obsservation:
# The hourly data conveys that the Uber trips decreases after midnight.
# It increases again after 5 am and it keep rising till 6 pm, which is the busiest hour for Uber and then the trips start decreasing.

# Now let’s analyze the Uber trips according to the weekdays:
sns.distplot(data_uber["Weekday"])

# Looking at the correlation of hours and weekdays on the Uber trips:
df = data_uber.groupby(["Weekday", "Hour"]).apply(lambda x: len(x))
df = df.unstack()
sns.heatmap(df, annot=False)

# Analyzing the density of Uber trips according to the regions of the New York city
data_uber.plot(kind='scatter', x='Lon', y='Lat', alpha=0.4, s=data_uber['Day'], label='Uber Trips',
figsize=(12, 8), cmap=plt.get_cmap('jet'))
plt.title("Uber Trips Analysis")
plt.legend()
plt.show()

