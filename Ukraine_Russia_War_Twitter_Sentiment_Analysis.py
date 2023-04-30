import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import nltk
import re
from nltk.corpus import stopwords
import string

data_tweet = pd.read_csv(r"C:\Users\prach\Desktop\New folder\filename\filename.csv")
# print(data_tweet.head())
# print(data_tweet.columns)
# We are creating a new dataframe that consists of following columns as they are only required for the sentiment analysis
data = data_tweet[["username", "tweet", "language"]]

# Checking if any null columns
# print(data.isnull().sum())
# It turns out there are no nulls present

# Checking tweets' count per language
count_tweet_lang = data["language"].value_counts()
# print(count_tweet_lang)
# total_tweet = count_tweet_lang.sum()
# print(885800/total_tweet) %age of a language' tweets
# Since English language tweet accounts for the 88 percent. So, we will only consider English tweets for this analysis.

#  We will remove all the links, punctuation, symbols and other language errors from the tweets
# nltk.download('stopwords')
stemmer = nltk.SnowballStemmer("english")
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
data["tweet"] = data["tweet"].apply(clean)

# We will be using  wordcloud of the tweets, which will show the most frequently used words in the tweets by people sharing their feelings and updates about the Ukraine and Russia war:
text = " ".join(i for i in data.tweet)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
plt.figure( figsize=(15,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
# plt.show()
# For Error-"Only supported for TrueType fonts", do
# 1.pip install --upgrade pip
# 2.pip install --upgrade Pillow

# We will be adding three more columns in this dataset as Positive, Negative, and Neutral by calculating the sentiment scores of the tweets:
# nltk.download('vader_lexicon')
sentiments = SentimentIntensityAnalyzer()
data["Positive"] = [sentiments.polarity_scores(i)["pos"] for i in data["tweet"]]
data["Negative"] = [sentiments.polarity_scores(i)["neg"] for i in data["tweet"]]
data["Neutral"] = [sentiments.polarity_scores(i)["neu"] for i in data["tweet"]]
data = data[["tweet", "Positive", "Negative", "Neutral"]]
print(data.head())

# We will look at the most frequent words used by people with positive sentiments:
positive =' '.join([i for i in data['tweet'][data['Positive'] > data["Negative"]]])
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(positive)
plt.figure( figsize=(15,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
# plt.show()

# We will look at the most frequent words used by people with negative sentiments:
negative =' '.join([i for i in data['tweet'][data['Negative'] > data["Positive"]]])
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(negative)
plt.figure( figsize=(15,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
# plt.show()

# Saving the data to a .csv file
data.to_csv(r'C:\Users\prach\Desktop\New folder\filename\SentimentAnalyzedData.csv', index=False)
