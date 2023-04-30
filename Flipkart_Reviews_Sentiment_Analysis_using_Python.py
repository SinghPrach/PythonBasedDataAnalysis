import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# Reading the data
data_flipkart = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/flipkart_reviews.csv")
# print(data.head())

# Checking if any columns contains any nulls
# print(data_flipkart.isnull().sum())
# No nulls found

# Preparing the column containing reviews for sentiment analysis
import nltk
import re
nltk.download('stopwords')
stemmer = nltk.SnowballStemmer("english")
from nltk.corpus import stopwords
import string
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
data_flipkart["Review"] = data_flipkart["Review"].apply(clean)

ratings = data_flipkart["Rating"].value_counts()
numbers = ratings.index
quantity = ratings.values

import plotly.express as px
figure_1 = px.pie(data_flipkart,
             values=quantity,
             names=numbers,hole = 0.5)
figure_1.show()

# Forming the wordcloud for better visualization
text = " ".join(i for i in data_flipkart.Review)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords,
                      background_color="white").generate(text)
plt.figure( figsize=(15,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
# Adding 3 new columns: Positive, Negative, and Neutral by calculating the sentiment scores of the reviews
# nltk.download('vader_lexicon')
sentiments = SentimentIntensityAnalyzer()
data_flipkart["Positive"] = [sentiments.polarity_scores(i)["pos"] for i in data_flipkart["Review"]]
data_flipkart["Negative"] = [sentiments.polarity_scores(i)["neg"] for i in data_flipkart["Review"]]
data_flipkart["Neutral"] = [sentiments.polarity_scores(i)["neu"] for i in data_flipkart["Review"]]
data_flipkart_reviews = data_flipkart[["Review", "Positive", "Negative", "Neutral"]]
print(data_flipkart_reviews.head())

# Looking at how the reviewers think about the products and services of Flipkart
x = sum(data_flipkart_reviews["Positive"])
y = sum(data_flipkart_reviews["Negative"])
z = sum(data_flipkart_reviews["Neutral"])

def sentiment_score(a, b, c):
    if (a>b) and (a>c):
        print("Positive 😊 ")
    elif (b>a) and (b>c):
        print("Negative 😠 ")
    else:
        print("Neutral 🙂 ")
sentiment_score(x, y, z)

# Looking at total of Positive, Negative, and Neutral sentiment scores
print("Positive: ", x)
print("Negative: ", y)
print("Neutral: ", z)
