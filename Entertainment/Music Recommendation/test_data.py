import unittest
import pandas as pd
from music_recommendation.src.data import load_data

class TestData(unittest.TestCase):

    def test_load_data(self):
        df = load_data('music_recommendation/data/song_data.csv')
        self.assertIsNotNone(df)
        self.assertIsInstance(df, pd.DataFrame)

    def test_data_shape(self):
        df = load_data('music_recommendation/data/song_data.csv')
        self.assertGreaterEqual(df.shape[0], 100)
        self.assertGreaterEqual(df.shape[1], 10)

if __name__ == '__main__':
    unittest.main()