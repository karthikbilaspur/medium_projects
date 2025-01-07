import unittest
from music_recommendation.src.app import App

class TestApp(unittest.TestCase):

    def test_init(self):
        app = App()
        self.assertIsNotNone(app)

    def test_run(self):
        app = App()
        app.run()
        self.assertTrue(app.is_running)

if __name__ == '__main__':
    unittest.main()