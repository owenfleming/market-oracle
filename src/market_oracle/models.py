class MarketEvent:
    """
    Represents a specific event (e.g., a game or an election) 
    from a specific data source.
    """
    def __init__(self, event_name: str, source_name: str, probability: float):
        self.event_name = event_name
        self.source_name = source_name
        self.probability = probability  # Expecting a decimal (e.g., 0.65 for 65%)

    def to_decimal_odds(self) -> float:
        """Converts percentage probability to decimal odds (e.g., 1.54)."""
        if self.probability <= 0:
            return 0.0
        return round(1 / self.probability, 2)

    def __repr__(self):
        """This tells Python how to 'print' the object so it's readable."""
        return f"[{self.source_name}] {self.event_name}: {self.probability*100}%"

class ComparisonResult:
    """
    An object specifically designed to hold the results of 
    comparing two different sources.
    """
    def __init__(self, event_a: MarketEvent, event_b: MarketEvent):
        self.event_a = event_a
        self.event_b = event_b
        self.discrepancy = abs(event_a.probability - event_b.probability)

    def report(self):
        """Prints a professional summary of the find."""
        print(f"--- Analysis: {self.event_a.event_name} ---")
        print(f"{self.event_a.source_name} Odds: {self.event_a.to_decimal_odds()}")
        print(f"{self.event_b.source_name} Odds: {self.event_b.to_decimal_odds()}")
        print(f"Edge Detected: {round(self.discrepancy * 100, 2)}%")