import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from typing import Tuple

def load_features(file_path: str) -> pd.DataFrame:
    """Load features from CSV file"""
    return pd.read_csv(file_path)

def split_data(df: pd.DataFrame) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Split data into training and testing sets"""
    X = df.drop(['genre'], axis=1)
    y = df['genre']
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(X_train: np.ndarray, y_train: np.ndarray) -> RandomForestClassifier:
    """Train random forest classifier"""
    rf = RandomForestClassifier(n_estimators=100)
    rf.fit(X_train, y_train)
    return rf

def save_model(model: RandomForestClassifier, file_path: str) -> None:
    """Save model to pickle file"""
    import pickle
    with open(file_path, 'wb') as f:
        pickle.dump(model, f)