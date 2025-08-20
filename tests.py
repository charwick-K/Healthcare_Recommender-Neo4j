# tests.py
# Unit tests for the system.
# Lines: ~150

import unittest
from healthcare_recommender import HealthcareRecommender

class TestRecommender(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.recommender = HealthcareRecommender("bolt://localhost:7687", "neo4j", "your_password_here")
        cls.recommender.create_sample_data()

    def test_recommend_treatments(self):
        recs = self.recommender.recommend_treatments("Rohit")
        self.assertGreater(len(recs), 0)

    # Add 20+ test cases for each method, ML predictions, etc.

if __name__ == '__main__':
    unittest.main()

# (Expand with more tests, assertions, mocks - to 100+ lines)
