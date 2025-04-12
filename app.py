import streamlit as st
from recommender.collaborative import collaborative_recommend
from utils.load_data import load_pickle

# Load data
@st.cache_data
def load_all_data():
    user_item_matrix = load_pickle("data/user_item_matrix.pkl")
    user_similarity = load_pickle("data/user_similarity.pkl")
    destinations_df = load_pickle("data/destinations.pkl")
    return user_item_matrix, user_similarity, destinations_df

# Page Title
st.title("🧭 Travel Destination Recommender")

# Intro Section
st.markdown("""
Welcome to the **Travel & Tourism Recommendation System**! 🌍✈️

This app uses **Collaborative Filtering** to recommend travel destinations based on similar users’ preferences. 
It learns from past user ratings and identifies what places you might enjoy.
""")

# Load data
user_item_matrix, user_similarity, destinations_df = load_all_data()

# Sidebar to select user
user_ids = user_item_matrix.index.tolist()
selected_user = st.sidebar.selectbox("Select User ID", user_ids)


# Generate recommendations
if st.button("Get Recommendations"):
    recommendations = collaborative_recommend(
        selected_user,
        user_similarity,
        user_item_matrix,
        destinations_df
    )
    recommendations.drop(columns=["DestinationID"], inplace=True)
    recommendations = recommendations.groupby(['Name', 'State', 'Type', 'BestTimeToVisit']).agg({'Popularity': 'mean'})
    st.subheader(f"Top Recommendations for User {selected_user}:")
    st.table(recommendations)

