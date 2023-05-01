import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
import string

df_email = pd.read_csv(r"C:\Users\prach\Desktop\New folder\EmailSpamPredData.csv")
print(df_email.head())

# Getting the size of the dataframe
print(df_email.shape)

# Getting the names of the columns of the dataframe
print(df_email.columns)

# Dropping the duplicates
df_email.drop_duplicates(inplace=True)
print(df_email.shape)

# Checking if missing data exists for any columns
print(df_email.isnull().sum())


# downloading the stopwords package
# nltk.download("stopwords")

# Function to clean the text and return the tokens
def process(text):
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join(nopunc)

    clean = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
    return clean


# to show the tokenization
df_email['text'].head().apply(process)

# Converting text to a matrix of tokens
from sklearn.feature_extraction.text import CountVectorizer

message = CountVectorizer(analyzer=process).fit_transform(df_email['text'])

# split the data into 80% training and 20% testing
from sklearn.model_selection import train_test_split

xtrain, xtest, ytrain, ytest = train_test_split(message, df_email['spam'], test_size=0.20, random_state=0)
# To see the shape of the data
print(message.shape)

# create and train the Naive Bayes Classifier
from sklearn.naive_bayes import MultinomialNB
classifier = MultinomialNB().fit(xtrain, ytrain)

print(classifier.predict(xtrain))
print(ytrain.values)

# Evaluating the model on the training data set
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
pred = classifier.predict(xtrain)
print(classification_report(ytrain, pred))
print()
print("Confusion Matrix: \n", confusion_matrix(ytrain, pred))
print("Accuracy: \n", accuracy_score(ytrain, pred))

#print the predictions
print(classifier.predict(xtest))
#print the actual values
print(ytest.values)

# Evaluating the model on the training data set
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
pred = classifier.predict(xtest)
print(classification_report(ytest, pred))
print()
print("Confusion Matrix: \n", confusion_matrix(ytest, pred))
print("Accuracy: \n", accuracy_score(ytest, pred))


