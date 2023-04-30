import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import string
import re
import plotly.express as px
# nltk.download('stopwords')

stemmer = nltk.SnowballStemmer("english")
tiktok_data = pd.read_csv(r"C:\Users\prach\Desktop\New folder\archive\tiktok_google_play_reviews.csv")
# print(tiktok_data.head())
# There are some columns with null values.

# In order to analyze TikTok reviews, we need two columns, content and score.
# Creating a new dataset with the above 2 mentioned columns.
new_ds = tiktok_data[["content", "score"]]
# print(new_ds.head())

# Checking if any of these 2 columns contains nulls.
# print(new_ds.isnull().sum())
# There are 16 nulls in 'content' column, so will drop them.
new_ds = new_ds.dropna()

# Cleaning the text in the content column in order to do the sentiment analysis.
stopword=set(stopwords.words('english'))
def clean(text):
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = [word for word in text.split(' ') if word not in stopword]
    text=" ".join(text)
    text = [stemmer.stem(word) for word in text.split(' ')]
    text=" ".join(text)
    return text
new_ds["content"] = new_ds["content"].apply(clean)

# Looking at the percentage of ratings given to TikTok at Google Play Store
ratings = new_ds["score"].value_counts()
numbers = ratings.index
quantity = ratings.values
figure_rating = px.pie(new_ds,
             values=quantity,
             names=numbers,hole = 0.5)
# figure_rating.show()
# print(numbers)

# Looking at the different kinds of words people use in their reviews.
# text = " ".join(i for i in new_ds.content)
# stopwords = set(STOPWORDS)
# wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
# plt.figure( figsize=(15,10))
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()

# Adding three more columns on the basis of sentimental scores, namely positive, negative, and neutral
# nltk.download('vader_lexicon')
sentiments = SentimentIntensityAnalyzer()
new_ds["Positive"] = [sentiments.polarity_scores(i)["pos"] for i in new_ds["content"]]
new_ds["Negative"] = [sentiments.polarity_scores(i)["neg"] for i in new_ds["content"]]
new_ds["Neutral"] = [sentiments.polarity_scores(i)["neu"] for i in new_ds["content"]]
data = new_ds[["content", "Positive", "Negative", "Neutral"]]
# print(data.head())

# Looking at words used in positive reviews
positive =' '.join([i for i in data['content'][data['Positive'] > data["Negative"]]])
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(positive)
plt.figure( figsize=(15,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# Looking at words used in negative reviews
negative =' '.join([i for i in data['content'][data['Negative'] > data["Positive"]]])
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(negative)
plt.figure( figsize=(15,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
