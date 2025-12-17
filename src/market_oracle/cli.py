"""Command line interface for Market Oracle."""

from market_oracle import MarketEvent, ComparisonResult


def main():
    print("🚀 Starting MarketOracle Analysis...\n")

    # 1. Create a "Prediction Market" object (e.g., from Polymarket)
    poly_event = MarketEvent(
        event_name="Lakers vs Celtics",
        source_name="Polymarket",
        probability=0.65  # 65% chance Lakers win
    )

    # 2. Create a "Sportsbook" object (e.g., from DraftKings)
    book_event = MarketEvent(
        event_name="Lakers vs Celtics",
        source_name="DraftKings",
        probability=0.55  # 55% chance Lakers win
    )

    # 3. Use your Comparison class to analyze them
    analysis = ComparisonResult(poly_event, book_event)
    analysis.report()


if __name__ == "__main__":
    main()