import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        result_1 = sentiment_analyzer('i love working with python')
        self.assertEqual(result_1['label'], 'SENT_POSITIVE')
        result_2 = sentiment_analyzer('i hate this python')
        self.assertEqual(result_2['label'], 'SENT_NEGATIVE')

if __name__ == '__main__':
    unittest.main()

# How to run test: python3.11 test_sentiment_analyzer.py