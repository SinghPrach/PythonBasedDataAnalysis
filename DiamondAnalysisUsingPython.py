# Dataset Link: https://github.com/amankharwal/Website-data/blob/master/diamonds.csv

import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\prach\Desktop\New folder\diamonds.csv")

print(df.head())

sum_price = df.price.sum()
print("Total Value of Diamonds: $", sum_price)

mean_price = df.price.mean()
print("Mean Value of Diamonds: $", mean_price)

# Summarizing the carat data
describe_carat = df.carat.describe()
print("Description of Carat: ", describe_carat)

# Summarizing a description of all non-numeric columns in this DataFrame
describe_nonNumeric = df.describe(include='object')
print("Description of Non-Numeric columns: ", describe_nonNumeric)

# Visualizing the data
import matplotlib.pyplot as plt

# Showing clarity of the diamond versus the carat size of the diamond
carat = df.carat
clarity = df.clarity
plt.scatter(clarity, carat)
plt.show()

# Using a bar plot to visualize the number of diamonds in each clarity type
clarityindexes = df["clarity"].value_counts().index.tolist()
claritycount = df["clarity"].value_counts().values.tolist()

print(clarityindexes)
print(claritycount)
plt.bar(clarityindexes, claritycount)
plt.show()

# Using Heat diagram to graphically show the correlations between numeric values in this dataframe
df = df.drop("Unnamed: 0", axis=1)
f, ax = plt.subplots(figsize=(10, 8))
corr = df.corr()
print(corr)

import seaborn
seaborn.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool),
                cmap=seaborn.diverging_palette(220, 10, as_cmap=True),
                square=True, ax=ax)
plt.show()
