from recommender.collaborative import collaborative_recommend
from utils.load_data import load_pickle

user_item_matrix = load_pickle("data/user_item_matrix.pkl")
user_similarity = load_pickle("data/user_similarity.pkl")
destinations_df = load_pickle("data/destinations.pkl")

def main():
    user_id = 15

    recommendations = collaborative_recommend(user_id, user_similarity, user_item_matrix, destinations_df)
    print("Top 5 recommendations for user", user_id)
    print(recommendations)

if __name__ == "__main__":
    main()
