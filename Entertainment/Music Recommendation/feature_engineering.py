import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from typing import Tuple

def extract_lyrics_features(df: pd.DataFrame) -> Tuple[np.ndarray, TfidfVectorizer]:
    """Extract TF-IDF features from song lyrics"""
    vectorizer = TfidfVectorizer(stop_words='english')
    lyrics_features = vectorizer.fit_transform(df['lyrics'])
    return lyrics_features, vectorizer

def extract_audio_features(df: pd.DataFrame) -> np.ndarray:
    """Extract audio features from song audio data"""
    return df.drop(['lyrics'], axis=1).values

def combine_features(lyrics_features: np.ndarray, audio_features: np.ndarray) -> np.ndarray:
    """Combine lyrics and audio features"""
    return np.concatenate((lyrics_features, audio_features), axis=1)