import unittest
import pandas as pd
from music_recommendation.src.model_evaluation import evaluate_model

class TestModelEvaluation(unittest.TestCase):

    def test_evaluate_model(self):
        model = train_model(pd.DataFrame([1, 2, 3, 4]), pd.DataFrame(['pop', 'rock', 'pop', 'rock']))
        X_test = pd.DataFrame([5, 6, 7, 8])
        y_test = pd.DataFrame(['pop', 'rock', 'pop', 'rock'])
        accuracy, report, matrix = evaluate_model(model, X_test, y_test)
        self.assertGreaterEqual(accuracy, 0)
        self.assertLessEqual(accuracy, 1)

if __name__ == '__main__':
    unittest.main()