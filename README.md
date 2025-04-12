# 🧭 Travel Destination Recommender System

This project is a **Collaborative Filtering-based Travel & Tourism Recommendation System** built using **Streamlit**. It suggests personalized travel destinations to users by analyzing preferences of similar users using a user-item rating matrix.

##  Features

- Recommends top destinations using collaborative filtering
- Interactive UI built with Streamlit
- Efficient data loading with Pickle
- Easily customizable and extendable

##  How It Works

1. Computes **cosine similarity** between users based on their travel ratings/preferences.
2. Identifies users most similar to the selected user.
3. Aggregates their destination ratings to suggest highly rated destinations.
4. Displays relevant details such as name, state, type, popularity, and best time to visit.


## 📦 Installation

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```
2. **Run the app:**
```bash
streamlit run app.py
```