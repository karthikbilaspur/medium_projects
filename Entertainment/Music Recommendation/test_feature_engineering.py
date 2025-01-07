import unittest
import pandas as pd
from music_recommendation.src.feature_engineering import extract_lyrics_features, extract_audio_features, combine_features

class TestFeatureEngineering(unittest.TestCase):

    def test_extract_lyrics_features(self):
        df = pd.DataFrame({'lyrics': ['happy lyrics', 'sad lyrics']})
        lyrics_features, vectorizer = extract_lyrics_features(df)
        self.assertEqual(lyrics_features.shape[1], 2)

    def test_extract_audio_features(self):
        df = pd.DataFrame({'danceability': [0.5, 0.7], 'energy': [0.3, 0.9]})
        audio_features = extract_audio_features(df)
        self.assertEqual(audio_features.shape[1], 2)

    def test_combine_features(self):
        lyrics_features = np.array([[0.5, 0.7], [0.3, 0.9]])
        audio_features = np.array([[0.2, 0.4], [0.6, 0.8]])
        combined_features = combine_features(lyrics_features, audio_features)
        self.assertEqual(combined_features.shape[1], 4)

if __name__ == '__main__':
    unittest.main()