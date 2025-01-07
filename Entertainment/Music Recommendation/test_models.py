import unittest
from music_recommendation.src.models import RandomForestClassifier

class TestModels(unittest.TestCase):

    def test_init(self):
        model = RandomForestClassifier()
        self.assertIsNotNone(model)

    def test_train(self):
        model = RandomForestClassifier()
        X_train = pd.DataFrame([1, 2, 3, 4])
        y_train = pd.DataFrame(['pop', 'rock', 'pop', 'rock'])
        model.train(X_train, y_train)
        self.assertTrue(model.is_trained)

if __name__ == '__main__':
    unittest.main()