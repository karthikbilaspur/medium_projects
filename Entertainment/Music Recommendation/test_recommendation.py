import unittest
import pandas as pd
from music_recommendation.src.recommendation_system import get_recommendations

class TestRecommendationSystem(unittest.TestCase):

    def test_get_recommendations(self):
        user_id = 1
        recommendations = get_recommendations(user_id)
        self.assertIsNotNone(recommendations)

if __name__ == '__main__':
    unittest.main()