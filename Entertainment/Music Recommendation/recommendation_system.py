import pandas as pd
from sklearn.neighbors import NearestNeighbors

def load_data(file_path):
    """Load data from CSV file"""
    return pd.read_csv(file_path)

def build_recommendation_system(df):
    """Build recommendation system using NearestNeighbors"""
    nn = NearestNeighbors(n_neighbors=5)
    nn.fit(df.drop(['genre'], axis=1))
    return nn

def get_recommendations(nn, user_id):
    """Get recommendations for a user"""
    distances, indices = nn.kneighbors(df.iloc[user_id].values.reshape(1, -1))
    return df.iloc[indices[0]]

if __name__ == '__main__':
    data_file_path = 'data/combined_features.csv'
    df = load_data(data_file_path)
    nn = build_recommendation_system(df)
    user_id = 0  # Replace with actual user ID
    recommendations = get_recommendations(nn, user_id)
    print(recommendations)