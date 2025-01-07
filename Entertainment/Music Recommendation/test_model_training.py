import unittest
import pandas as pd
from music_recommendation.src.model_training import train_model, save_model

class TestModelTraining(unittest.TestCase):

    def test_train_model(self):
        df = pd.DataFrame({'features': [1, 2, 3, 4], 'genre': ['pop', 'rock', 'pop', 'rock']})
        X_train, X_test, y_train, y_test = train_test_split(df['features'], df['genre'], test_size=0.2)
        model = train_model(X_train, y_train)
        self.assertIsNotNone(model)

    def test_save_model(self):
        model = train_model(pd.DataFrame([1, 2, 3, 4]), pd.DataFrame(['pop', 'rock', 'pop', 'rock']))
        save_model(model, 'music_recommendation/models/test_model.pkl')
        self.assertTrue(os.path.exists('music_recommendation/models/test_model.pkl'))

if __name__ == '__main__':
    unittest.main()