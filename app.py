import pickle
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

# Load the pickle files
with open('tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)
with open('SVM.pkl', 'rb') as f:
    model = pickle.load(f)

# Define streamlit app
st.title('Sentiment Analysis App')
st.write('Enter a sentence to analyze its sentiment:')

# Get user input
user_input = st.text_input('Enter a sentence')

# Predicting sentiment
if st.button('Predict'):
    if user_input:
        input_tfidf = vectorizer.transform([user_input])
        prediction = model.predict(input_tfidf)[0]
        st.write(f'The sentiment of the sentence is: {prediction}')
    else:
        st.write('Please enter a sentence')
