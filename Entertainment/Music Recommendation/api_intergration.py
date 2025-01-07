import pandas as pd
import numpy as np
from typing import Tuple

def load_data(file_path: str) -> pd.DataFrame:
    """Load data from CSV file"""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Handle missing values in the dataset"""
    return df.fillna(df.mean())

def preprocess_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Preprocess data by handling missing values and encoding categorical variables"""
    df = handle_missing_values(df)
    categorical_cols = ['genre', 'emotions']
    df[categorical_cols] = df[categorical_cols].apply(lambda x: pd.Categorical(x).codes)
    return df.drop(['lyrics'], axis=1), df['lyrics']

def save_preprocessed_data(df: pd.DataFrame, file_path: str) -> None:
    """Save preprocessed data to CSV file"""
    df.to_csv(file_path, index=False)