import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from typing import Tuple

def load_model(file_path: str) -> RandomForestClassifier:
    """Load model from pickle file"""
    import pickle
    with open(file_path, 'rb') as f:
        model = pickle.load(f)
    return model

def load_data(file_path: str) -> pd.DataFrame:
    """Load data from CSV file"""
    return pd.read_csv(file_path)

def evaluate_model(model: RandomForestClassifier, X_test: np.ndarray, y_test: np.ndarray) -> Tuple[float, str, np.ndarray]:
    """Evaluate model performance"""
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    matrix = confusion_matrix(y_test, y_pred)
    return accuracy, report, matrix