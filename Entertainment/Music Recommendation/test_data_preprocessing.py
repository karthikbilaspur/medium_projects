import unittest
import pandas as pd
from music_recommendation.src.data_preprocessing import load_data, handle_missing_values, preprocess_data

class TestDataPreprocessing(unittest.TestCase):

    def test_load_data(self):
        file_path = 'music_recommendation/data/song_data.csv'
        df = load_data(file_path)
        self.assertIsNotNone(df)
        self.assertIsInstance(df, pd.DataFrame)

    def test_handle_missing_values(self):
        df = pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': [5, np.nan, 7, 8]})
        df = handle_missing_values(df)
        self.assertFalse(df.isnull().values.any())

    def test_preprocess_data(self):
        df = pd.DataFrame({'lyrics': ['happy lyrics', 'sad lyrics'], 'genre': ['pop', 'rock']})
        X, y = preprocess_data(df)
        self.assertEqual(X.shape[1], 2)
        self.assertEqual(y.shape[0], 2)

if __name__ == '__main__':
    unittest.main()