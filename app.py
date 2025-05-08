import pickle
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import time

# Load the vectorizer and model
with open('tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open('SVM.pkl', 'rb') as f:
    model = pickle.load(f)

# Set up page config
st.set_page_config(page_title='Sentiment Analysis App', page_icon='💬', layout='centered')

# Title and Description
st.markdown("<h1 style='text-align: center;'>💬 Sentiment Analysis App</h1>", unsafe_allow_html=True)
st.write("Type a sentence below and discover its **sentiment** instantly!")

# Text input
user_input = st.text_input("✏️ Enter your sentence:")

# Predict button
if st.button('🔍 Predict Sentiment'):
    if user_input.strip() != "":
        with st.spinner('Analyzing sentiment... 🔄'):
            time.sleep(1.5)  # Simulate loading animation
            input_tfidf = vectorizer.transform([user_input])
            prediction = model.predict(input_tfidf)[0]

        # Display results with effects
        if prediction.lower() == 'positive':
            st.success(f'✅ The sentiment is **Positive**')
            st.balloons()
        elif prediction.lower() == 'negative':
            st.error(f'❌ The sentiment is **Negative**')
            st.snow()
        else:
            st.info(f'ℹ️ The sentiment is **{prediction}**')
    else:
        st.warning('⚠️ Please enter a sentence before clicking Predict.')
