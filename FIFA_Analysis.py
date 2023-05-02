import numpy as np
import pandas as pd

# for visualizations
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

data_fifa = pd.read_csv(r"C:\Users\prach\Desktop\New folder\fifa_data.csv")
print(data_fifa.shape)

print(data_fifa.head())


# Method to check for players country-wise
def country(x):  # x=country name
    return data_fifa[data_fifa['Nationality'] == x][['Name', 'Overall', 'Potential', 'Position']]


# Checking for the Indian Players
print(country('India'))

# print(data_fifa.columns)

# Method to check for players club-wise
def club(x):
    return data_fifa[data_fifa['Club'] == x][['Name','Jersey Number','Position','Overall','Nationality','Age','Wage',
                                    'Value','Contract Valid Until']]

print(club('Manchester United'))

# Describing the datset
# print(data_fifa.describe())

# print(data_fifa.isnull().sum())

# Replacing the missing values of the columns
data_fifa['ShortPassing'].fillna(data_fifa['ShortPassing'].mean(), inplace = True)
data_fifa['Volleys'].fillna(data_fifa['Volleys'].mean(), inplace = True)
data_fifa['Dribbling'].fillna(data_fifa['Dribbling'].mean(), inplace = True)
data_fifa['Curve'].fillna(data_fifa['Curve'].mean(), inplace = True)
data_fifa['FKAccuracy'].fillna(data_fifa['FKAccuracy'], inplace = True)
data_fifa['LongPassing'].fillna(data_fifa['LongPassing'].mean(), inplace = True)
data_fifa['BallControl'].fillna(data_fifa['BallControl'].mean(), inplace = True)
data_fifa['HeadingAccuracy'].fillna(data_fifa['HeadingAccuracy'].mean(), inplace = True)
data_fifa['Finishing'].fillna(data_fifa['Finishing'].mean(), inplace = True)
data_fifa['Crossing'].fillna(data_fifa['Crossing'].mean(), inplace = True)
data_fifa['Weight'].fillna('200lbs', inplace = True)
data_fifa['Contract Valid Until'].fillna(2019, inplace = True)
data_fifa['Height'].fillna("5'11", inplace = True)
data_fifa['Loaned From'].fillna('None', inplace = True)
data_fifa['Joined'].fillna('Jul 1, 2018', inplace = True)
data_fifa['Jersey Number'].fillna(8, inplace = True)
data_fifa['Body Type'].fillna('Normal', inplace = True)
data_fifa['Position'].fillna('ST', inplace = True)
data_fifa['Club'].fillna('No Club', inplace = True)
data_fifa['Work Rate'].fillna('Medium/ Medium', inplace = True)
data_fifa['Skill Moves'].fillna(data_fifa['Skill Moves'].median(), inplace = True)
data_fifa['Weak Foot'].fillna(3, inplace = True)
data_fifa['Preferred Foot'].fillna('Right', inplace = True)
data_fifa['International Reputation'].fillna(1, inplace = True)
data_fifa['Wage'].fillna('€200K', inplace = True)
data_fifa.fillna(0, inplace = True)

# print(data_fifa.isnull().sum())

# Methods for different scenarios
def defending(data):
    return int(round((data[['Marking', 'StandingTackle',
                               'SlidingTackle']].mean()).mean()))

def general(data):
    return int(round((data[['HeadingAccuracy', 'Dribbling', 'Curve',
                               'BallControl']].mean()).mean()))

def mental(data):
    return int(round((data[['Aggression', 'Interceptions', 'Positioning',
                               'Vision','Composure']].mean()).mean()))

def passing(data):
    return int(round((data[['Crossing', 'ShortPassing',
                               'LongPassing']].mean()).mean()))

def mobility(data):
    return int(round((data[['Acceleration', 'SprintSpeed',
                               'Agility','Reactions']].mean()).mean()))
def power(data):
    return int(round((data[['Balance', 'Jumping', 'Stamina',
                               'Strength']].mean()).mean()))

def rating(data):
    return int(round((data[['Potential', 'Overall']].mean()).mean()))

def shooting(data):
    return int(round((data[['Finishing', 'Volleys', 'FKAccuracy',
                               'ShotPower','LongShots', 'Penalties']].mean()).mean()))

# Renaming the columns
data_fifa.rename(columns={'Club Logo':'Club_Logo'}, inplace=True)

# adding these categories to the data

data_fifa['Defending'] = data_fifa.apply(defending, axis = 1)
data_fifa['General'] = data_fifa.apply(general, axis = 1)
data_fifa['Mental'] = data_fifa.apply(mental, axis = 1)
data_fifa['Passing'] = data_fifa.apply(passing, axis = 1)
data_fifa['Mobility'] = data_fifa.apply(mobility, axis = 1)
data_fifa['Power'] = data_fifa.apply(power, axis = 1)
data_fifa['Rating'] = data_fifa.apply(rating, axis = 1)
data_fifa['Shooting'] = data_fifa.apply(shooting, axis = 1)

# Preparing a dataset for players
players = data_fifa[['Name','Defending','General','Mental','Passing',
                'Mobility','Power','Rating','Shooting','Flag','Age',
                'Nationality', 'Photo', 'Club_Logo', 'Club']]

players.head()


# some_clubs = ('CD Leganés', 'Southampton', 'RC Celta', 'Empoli', 'Fortuna Düsseldorf', 'Manchestar City',
#              'Tottenham Hotspur', 'FC Barcelona', 'Valencia CF', 'Chelsea', 'Real Madrid')
#
# data_club = data_fifa.loc[data_fifa['Club'].isin(some_clubs) & data_fifa['Wage']]
#
# plt.rcParams['figure.figsize'] = (16, 8)
# ax = sns.boxplot(x = 'Club', y = 'Wage', data = data_club, palette = 'Reds')
# ax.set_xlabel(xlabel = 'Names of some popular Clubs', fontsize = 10)
# ax.set_ylabel(ylabel = 'Distribution', fontsize = 10)
# ax.set_title(label = 'Disstribution of Wages in some Popular Clubs', fontsize = 20)
# plt.xticks(rotation = 90)
# plt.show()

# # Showing different nations participating
# plt.style.use('dark_background')
# data_fifa['Nationality'].value_counts().head(80).plot.bar(color = 'orange', figsize = (20, 7))
# plt.title('Different Nations Participating in FIFA 2019', fontsize = 30, fontweight = 20)
# plt.xlabel('Name of The Country')
# plt.ylabel('count')
# plt.show()

# Countries with most players
print(data_fifa['Nationality'].value_counts().head(8))

# Finding the popular club
data_fifa['Club'].value_counts().head(10)
