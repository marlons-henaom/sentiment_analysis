from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class test_sentiment_analyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):

        # Prueba 1
        result_1 = sentiment_analyzer('I love working with Python')
        self.assertEqual(result_1["label"], "SENT_POSITIVE")

        # Prueba 2
        result_2 = sentiment_analyzer('I hate working with Python')
        self.assertEqual(result_2["label"], "SENT_NEGATIVE")

        # Prueba 3
        result_3 = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(result_3["label"], "SENT_NEUTRAL")

unittest.main()