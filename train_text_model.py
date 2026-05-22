import pandas as pd

df = pd.read_csv('datasets/text_emotion.csv')
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['emotion']
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X, y)
import pickle

pickle.dump(model, open('models/text_emotion_model.pkl','wb'))
pickle.dump(vectorizer, open('models/vectorizer.pkl','wb'))