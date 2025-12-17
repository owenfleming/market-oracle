import unittest
from market_oracle import MarketEvent, ComparisonResult


class TestMarketEvent(unittest.TestCase):
    def test_to_decimal_odds(self):
        event = MarketEvent("Test Event", "Test Source", 0.5)
        self.assertEqual(event.to_decimal_odds(), 2.0)

    def test_repr(self):
        event = MarketEvent("Test Event", "Test Source", 0.5)
        self.assertEqual(repr(event), "[Test Source] Test Event: 50.0%")


class TestComparisonResult(unittest.TestCase):
    def test_discrepancy(self):
        event_a = MarketEvent("Event", "A", 0.6)
        event_b = MarketEvent("Event", "B", 0.5)
        comparison = ComparisonResult(event_a, event_b)
        self.assertAlmostEqual(comparison.discrepancy, 0.1)


if __name__ == "__main__":
    unittest.main()