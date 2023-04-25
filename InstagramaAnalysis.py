import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

from sklearn.model_selection import train_test_split
# from sklearn.linear_model import PassiveAggressiveRegressor
#
# reading the data
imp_data = pd.read_csv("Instagram data.csv", encoding='latin1')
# print(imp_data.head())

# Checking null values
# print(imp_data.isnull().sum())

# Dropping null values, in case
# imp_data = imp_data.dropna()

imp_data.info()

# Distribution of impressions (displot or histplot)
# plt.figure(figsize=(10, 8))
# plt.style.use('fivethirtyeight')
# plt.title("Distribution of Impressions From Home")
# sns.displot(imp_data['From Home'])
# plt.show()
#
# plt.figure(figsize=(10, 8))
# plt.title("Distribution of Impressions From Hashtags")
# sns.displot(imp_data['From Hashtags'])
# plt.show()
#
# plt.figure(figsize=(10, 8))
# plt.title("Distribution of Impressions From Explore")
# sns.displot(imp_data['From Explore'])
# plt.show()

# Sum of all the impressions
home = imp_data["From Home"].sum()
hashtags = imp_data["From Hashtags"].sum()
explore = imp_data["From Explore"].sum()
other = imp_data["From Other"].sum()

# label_fig = ['From Home', 'From Hashtags', 'From Explore', 'Other']
# value_fig = [home, hashtags, explore, other]
#
# fig_various_sources = px.pie(imp_data, values=value_fig, names=label_fig,
#                              title='Impressions on Instagram Posts From Various Sources', hole=0.5)
# fig_various_sources.show()

# Analyzing Captions and Hashtags
# text_caption = " ".join(i for i in imp_data.Caption)
# stopwords_caption = set(STOPWORDS)
# wordcloud_caption = WordCloud(stopwords=stopwords_caption, background_color="white").generate(text_caption)
# plt.style.use('classic')
# plt.figure( figsize=(12,10))
# plt.imshow(wordcloud_caption, interpolation='bilinear')
# plt.axis("off")
# plt.show()

# Advantages of Word Clouds :
# Analyzing customer and employee feedback.
# Identifying new SEO keywords to target.

# text_hashtag = " ".join(i for i in imp_data.Hashtags)
# stopwords_hashtag = set(STOPWORDS)
# wordcloud_hashtag = WordCloud(stopwords=stopwords_hashtag, background_color="white").generate(text_hashtag)
# plt.figure( figsize=(12,10))
# plt.imshow(wordcloud_hashtag, interpolation='bilinear')
# plt.axis("off")
# plt.show()

# scatter plots

# figure_Likes = px.scatter(data_frame = imp_data, x="Impressions",
#                     y="Likes", size="Likes",
#                     title = "Relationship Between Likes and Impressions")
# figure_Likes.show()
#
# figure_Comments = px.scatter(data_frame = imp_data, x="Impressions",
#                     y="Comments", size="Comments",
#                     title = "Relationship Between Comments and Total Impressions")
# figure_Comments.show()
#
# figure_Shares = px.scatter(data_frame = imp_data, x="Impressions",
#                     y="Shares", size="Shares",
#                     title = "Relationship Between Shares and Total Impressions")
# figure_Shares.show()
#
# figure_Saves = px.scatter(data_frame = imp_data, x="Impressions",
#                     y="Saves", size="Saves",
#                     title = "Relationship Between Post Saves and Total Impressions")
# figure_Saves.show()

# Correlation is a statistical measure that expresses the extent to which two variables are linearly related (meaning
# they change together at a constant rate).
correlation = (imp_data.corr())
# print(correlation)
# print(correlation["Impressions"].sort_values(ascending=False))

conversion_rate = (imp_data["Follows"].sum() / imp_data["Profile Visits"].sum()) * 100
print(conversion_rate)
#
figure_ProfileVisits = px.scatter(data_frame = imp_data, x="Profile Visits",
                    y="Follows", size="Follows",
                    title = "Relationship Between Profile Visits and Followers Gained")
figure_ProfileVisits.show()
# Instagram Reach Prediction Model
x = np.array(imp_data[['Likes', 'Saves', 'Comments', 'Shares',
                   'Profile Visits', 'Follows']])
y = np.array(imp_data["Impressions"])
# xtrain, xtest, ytrain, ytest = train_test_split(x, y,
#                                                 test_size=0.2,
#                                                 random_state=42)

# Now here’s is how we can train a machine learning model to predict the reach of an Instagram post using Python:
#
# model = PassiveAggressiveRegressor()
# model.fit(xtrain, ytrain)
# model.score(xtest, ytest)
#
# # Features = [['Likes','Saves', 'Comments', 'Shares', 'Profile Visits', 'Follows']]
# features = np.array([[282.0, 233.0, 4.0, 9.0, 165.0, 54.0]])
# model.predict(features)
