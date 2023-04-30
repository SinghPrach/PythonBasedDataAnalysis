# Importing the libraries that we'd require
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
# To use trendline feature, first do 'pip install statsmodels'

# Dataset Link:https://raw.githubusercontent.com/amankharwal/Website-data/master/tips.csv

tips_data = pd.read_csv(r"C:\Users\prach\Desktop\tips.csv")
# print(tips_data.head())

# Dataset descriptions
# total_bill: Total bill in dollars including tax
# tip: Tip given to waiter in dollars
# sex: gender of the person paying the bill
# smoker: whether the person smoked or not
# day: day of the week
# time: lunch or dinner
# size: number of people

# Analyzing the tips given to the waiters according to:
# the total bill paid
# number of people at a table
# and the day of the week:
figure_1 = px.scatter(data_frame = tips_data, x="total_bill",
                    y="tip", size="size", color= "day",trendline="ols")
figure_1.show()

# On the basis of
# the total bill paid
# the number of people at a table
# and the gender of the person paying the bill:
figure_2 = px.scatter(data_frame = tips_data, x="total_bill",
                    y="tip", size="size", color= "sex", trendline="ols")
figure_2.show()

# On the basis of
# the total bill paid
# the number of people at a table
# and the time of the meal:
figure_3 = px.scatter(data_frame = tips_data, x="total_bill",
                    y="tip", size="size", color= "time", trendline="ols")
figure_3.show()

# Let's find out which day the waiters were tipped the most
figure_4 = px.pie(tips_data,
             values='tip',
             names='day',hole = 0.5)
figure_4.show()

# Let's find out which gender tipped the waiters most
figure_5 = px.pie(tips_data,
             values='tip',
             names='sex',hole = 0.5)
figure_5.show()

# Let's find out if the smoker tips more or the non-smoker
figure_6 = px.pie(tips_data,
             values='tip',
             names='smoker',hole = 0.5)
figure_6.show()

# Let's find out if waiters are tipped most during lunch or dinner
figure_7 = px.pie(tips_data,
             values='tip',
             names='time',hole = 0.5)
figure_7.show()

# Building a Prediction Model
# Before training a waiter tips prediction model, we need to do some data transformation by transforming the categorical values into numerical values:
tips_data["sex"] = tips_data["sex"].map({"Female": 0, "Male": 1})
tips_data["smoker"] = tips_data["smoker"].map({"No": 0, "Yes": 1})
tips_data["day"] = tips_data["day"].map({"Thur": 0, "Fri": 1, "Sat": 2, "Sun": 3})
tips_data["time"] = tips_data["time"].map({"Lunch": 0, "Dinner": 1})
# print(tips_data.head())

x = np.array(tips_data[["total_bill", "sex", "smoker", "day",
                   "time", "size"]])
y = np.array(tips_data["tip"])

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x, y,
                                                test_size=0.2,
                                                random_state=42)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(xtrain, ytrain)

# features = [[total_bill, "sex", "smoker", "day", "time", "size"]]
features = np.array([[2450, 0, 1, 2, 1, 4]])
predicted_tip = model.predict(features)
print(predicted_tip)
