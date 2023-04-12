import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# Reading
imp_data = pd.read_csv("dailyActivity_merged.csv")
# print(imp_data.head())

# Checking if dataset has nulls
# print(imp_data.isnull().sum())
# This data set does not have any null values.

# Getting information about its columns
# print(imp_data.info())
# An object datatype is a string in pandas so it performs a string operation instead of a mathematical one.

# Changing Datatype of Object dtype column
imp_data["ActivityDate"] = pd.to_datetime(imp_data["ActivityDate"])
# print(imp_data.info())

# Adding a new column
imp_data["TotalMinutes"] = imp_data["VeryActiveMinutes"] + imp_data["FairlyActiveMinutes"] + imp_data[
    "LightlyActiveMinutes"] + imp_data["SedentaryMinutes"]
# print(imp_data["TotalMinutes"].sample(5))

# Looking at the descriptive statistics of the dataset
# print(imp_data.describe())

# Analyzing the data
# Relationship between calories burned and total steps walked
relatecaloriesteps = px.scatter(data_frame=imp_data, x="Calories",
                                y="TotalSteps", size="VeryActiveMinutes",
                                title="Relationship Between Calories & Total Steps")
relatecaloriesteps.show()
# Observations
# 1. The relationship Between Calories & Total Steps is almost linear in nature.

# Looking at the average total number of active minutes in a day
label = ["Very Active Minutes", "Fairly Active Minutes",
         "Lightly Active Minutes", "Inactive Minutes"]
counts = imp_data[["VeryActiveMinutes", "FairlyActiveMinutes",
               "LightlyActiveMinutes", "SedentaryMinutes"]].mean()
colors = ['gold','lightgreen', "pink", "blue"]

fig_active = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig_active.update_layout(title_text='Total Active Minutes')
fig_active.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig_active.show()
# The head() method returns a specified number of rows, string from the top.
# The head() method returns the first 5 rows if a number is not specified.
# Observations
# 1. Inactive Minutes- 81.3%
# 2. Lightly Active Minutes- 15.8%
# 3. Fairly Active Minutes- 1.11%
# 4. Very Active Minutes- 1.74%

# Finding weekdays and adding a new column of day to the dataset
imp_data["Day"] = imp_data["ActivityDate"].dt.day_name()
print(imp_data["Day"].head())

# Active minutes on each day of the week
fig_active_day = go.Figure()
fig_active_day.add_trace(go.Bar(
    x=imp_data["Day"],
    y=imp_data["VeryActiveMinutes"],
    name='Very Active',
    marker_color='purple'
))
fig_active_day.add_trace(go.Bar(
    x=imp_data["Day"],
    y=imp_data["FairlyActiveMinutes"],
    name='Fairly Active',
    marker_color='green'
))
fig_active_day.add_trace(go.Bar(
    x=imp_data["Day"],
    y=imp_data["LightlyActiveMinutes"],
    name='Lightly Active',
    marker_color='pink'
))
fig_active_day.update_layout(barmode='group', xaxis_tickangle=-45)
fig_active_day.show()


# Taking a look at the inactive minutes for different days of the week
day = imp_data["Day"].value_counts()
label = day.index
counts = imp_data["SedentaryMinutes"]
colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]

fig_inactive_day = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig_inactive_day.update_layout(title_text='Inactive Minutes Daily')
fig_inactive_day.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig_inactive_day.show()

# Observations
# 1. Least inactive day- Sunday
# 2. Most inactive day- Thursday

# Calories burned on each day of the week

calories = imp_data["Day"].value_counts()
label = calories.index
counts = imp_data["Calories"]
colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]

fig_calories_burned = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig_calories_burned.update_layout(title_text='Calories Burned Daily')
fig_calories_burned.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig_calories_burned.show()
# Observations
# 1. Most calories burned- Tuesday
# 2. Least calories burned- Sunday
