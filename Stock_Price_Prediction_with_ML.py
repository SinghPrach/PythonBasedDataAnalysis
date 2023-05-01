import pandas as pd

# Dataset Link: https://www.nseindia.com/get-quotes/equity?symbol=ICICIBANK

data_icici1 = pd.read_csv(r"C:\Users\prach\Desktop\New folder\StockPredict\Quote-Equity-ICICIBANK-EQ-01-05-2022-to-01-05-2023.csv")

# Reversing the rows order, to ensure it has latest later
data_icici = data_icici1[::-1]
print(data_icici.head())
# Remove spaces from column names
data_icici.columns = data_icici.columns.str.replace(' ', '')
# Printing the number of training days
print("Training days =",data_icici.shape)
data_icici.reset_index(inplace = True, drop = True)
print(data_icici.head())

# Visualizing the close price data
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
# plt.figure(figsize=(10, 4))
#
# plt.plot(data_icici["close"])x=data_icici['Date']
# # y=data_icici['close']
# # plt.plot(x, y)
# # plt.title("ICICI's Stock Price")
# # plt.xlabel("Dates")
# # plt.ylabel("Close Price (INR)")
# plt.show()

# Getting the close price
icici_close = data_icici[["close"]]
print(icici_close.head())

# Creating a variable to predict ‘X’ days, from today in the future:
futureDays = 25

# Creating a new target column shifted ‘X’ units/days up:
icici_close["Prediction"] = icici_close[["close"]].shift(-futureDays)
print(icici_close.head())
print(icici_close.tail())

# Creating a future dataset (x) and convert into a numpy array and remove last ‘x’ rows/days:
import numpy as np
x = np.array(icici_close.drop(["Prediction"], 1))[:-futureDays]
print(x)

# Creating a target dataset (y) and convert it to a numpy array and get all of the target values except the last ‘x’ rows days:
y = np.array(icici_close["Prediction"])[:-futureDays]
print(y)
#
# Splitting the data into 75% training and 25% testing
from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.25)

# Creating models
# Creating the decision tree regressor model
from sklearn.tree import DecisionTreeRegressor
tree = DecisionTreeRegressor().fit(xtrain, ytrain)

# creating the Linear Regression model
from sklearn.linear_model import LinearRegression
linear = LinearRegression().fit(xtrain, ytrain)

# Getting the last ‘x’ rows/days of the feature dataset
xfuture = icici_close.drop(["Prediction"], 1)[:-futureDays]
xfuture = xfuture.tail(futureDays)
xfuture = np.array(xfuture)
# print(xfuture)

# To see the model tree prediction
treePrediction = tree.predict(xfuture)
print("Decision Tree prediction =",treePrediction)

# To see the model linear regression prediction
linearPrediction = linear.predict(xfuture)
print("Linear regression Prediction =",linearPrediction)

# Visualizing Decision Tree Prediction
predictions = treePrediction

valid = icici_close[x.shape[0]:]
valid["Predictions"] = predictions
plt.figure(figsize=(10, 6))
plt.title("ICICI's Stock Price Prediction Model(Decision Tree Regressor Model)")
plt.xlabel("Days")
plt.ylabel("Close Price in INR")
plt.plot(icici_close["close"])
plt.plot(valid[["close", "Predictions"]])
plt.legend(["Original", "Valid", "Predictions"])
plt.show()

# Visualizing the linear model predictions
predictions = linearPrediction
valid = icici_close[x.shape[0]:]
valid["Predictions"] = predictions
plt.figure(figsize=(10, 6))
plt.title("ICICI's Stock Price Prediction Model(Linear Regression Model)")
plt.xlabel("Days")
plt.ylabel("Close Price in INR")
plt.plot(icici_close["close"])
plt.plot(valid[["close", "Predictions"]])
plt.legend(["Original", "Valid", "Predictions"])
plt.show()
