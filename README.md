# **Sentiment Analysis Web App**  

🚀 **Live Demo**: [Sentiment Analysis Web App](https://sentiment-analysis-nlp-1.streamlit.app/)  

## 📌 **Overview**  
This web application predicts the sentiment of user-input text (Positive or Negative) using a pre-trained **Support Vector Machine (SVM)** model and **TF-IDF** vectorization. It allows users to easily classify text sentiment in real time.

## 🛠 **Features**  
- 📄 **Simple User Interface**: Input a sentence to analyze its sentiment.
- 🔮 **Real-Time Sentiment Prediction**: Get instant sentiment predictions (Positive/Negative) for any sentence.
- 🧑‍💻 **Machine Learning Model**: Uses a trained SVM model for accurate sentiment classification.
- 📥 **Instant Feedback**: Displays the predicted sentiment immediately after the input.

## 🚀 **How to Use**  
1. **Enter a Sentence**: Type a sentence into the input field.  
2. **Click "Predict"**: The app will analyze and predict whether the sentiment is Positive or Negative.  
3. **View Prediction**: See the sentiment prediction below the input field.  

## 🏗 **Deployment Details**  
- **Framework**: Streamlit  
- **Model**: SVM (Support Vector Machine)  
- **Feature Extraction**: TF-IDF Vectorization  
- **Hosting**: Deployed via [Streamlit Cloud](https://streamlit.io/)  

## ⚡ **Run Locally**  
To run the app on your local machine:  
```bash
# Clone the repository
git clone https://github.com/your-username/sentiment-analysis.git
cd sentiment-analysis

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
````

## 📁 **Project Structure**

```
sentiment-analysis/
├── app.py                 # Streamlit app script
├── tfidf_vectorizer.pkl   # Saved TF-IDF vectorizer
├── SVM.pkl                # Trained SVM model
├── Sentiment_Analysis.ipynb  # Jupyter notebook for sentiment analysis workflow
├── IPhone 16 all variants Amazon reviews.xlsx  # Dataset for iPhone 16 variants reviews
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## 📦 **requirements.txt**

This file should include the following dependencies:

```
streamlit
scikit-learn
pandas
numpy
```

---
