# Market Oracle

A Python package to compare prediction markets with traditional betting markets, helping identify arbitrage opportunities and market inefficiencies.

## Features

- Compare probabilities from different market sources
- Calculate decimal odds conversions
- Detect discrepancies between markets
- Command-line interface for quick analysis

## Installation

### From Source

```bash
git clone https://github.com/yourusername/market-oracle.git
cd market-oracle
pip install -e .
```

### Development

```bash
pip install -e ".[dev]"
```

## Usage

### Command Line

```bash
market-oracle
```

### Python API

```python
from market_oracle import MarketEvent, ComparisonResult

# Create market events
poly_event = MarketEvent("Lakers vs Celtics", "Polymarket", 0.65)
book_event = MarketEvent("Lakers vs Celtics", "DraftKings", 0.55)

# Compare them
analysis = ComparisonResult(poly_event, book_event)
analysis.report()
```

## Testing

```bash
pytest
```

## License

MIT
