import unittest
from music_recommendation.src.utils import load_config

class TestUtils(unittest.TestCase):

    def test_load_config(self):
        config = load_config('music_recommendation/config.json')
        self.assertIsNotNone(config)
        self.assertIsInstance(config, dict)

if __name__ == '__main__':
    unittest.main()