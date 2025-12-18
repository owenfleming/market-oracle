import requests
import json
from src.models import MarketEvent

class BaseFetcher:
    def fetch(self):
        raise NotImplementedError()

class PolymarketFetcher(BaseFetcher):
    def __init__(self):
        self.gamma_url = "https://gamma-api.polymarket.com"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    def get_market(self, identifier: str) -> MarketEvent:
        if identifier.isdigit():
            return self.fetch_by_id(identifier)
        return self.fetch_by_slug(identifier)

    def fetch_by_id(self, market_id: str) -> MarketEvent:
        """Direct lookup that guarantees full market data."""
        response = requests.get(
            f"{self.gamma_url}/markets/{market_id}", 
            headers=self.headers
        )
        return self._process_single_market(response)

    def fetch_by_slug(self, slug: str) -> MarketEvent:
        print(f"   (Debug) Searching for Event: {slug}...")
        
        # 1. Try to find the EVENT first
        event_response = requests.get(
            f"{self.gamma_url}/events", 
            params={"slug": slug}, 
            headers=self.headers
        )
        
        if event_response.status_code == 200:
            events = event_response.json()
            if events:
                first_event = events[0]
                markets = first_event.get('markets', [])
                if markets:
                    # CRITICAL FIX: The event payload might be missing prices.
                    # We take the ID and do a fresh lookup to be 100% sure.
                    market_id = markets[0].get('id')
                    print(f"   (Debug) -> Event found! Fetching full details for Market ID: {market_id}")
                    return self.fetch_by_id(market_id)

        # 2. Fallback: Try it as a direct Market slug
        print(f"   (Debug) Event not found. Trying Market slug...")
        market_response = requests.get(
            f"{self.gamma_url}/markets", 
            params={"slug": slug}, 
            headers=self.headers
        )
        
        if market_response.status_code == 200:
            markets = market_response.json()
            if markets:
                return self._map_market_data(markets[0])
                
        return None

    def _process_single_market(self, response):
        if response.status_code == 200:
            return self._map_market_data(response.json())
        return None

    def _map_market_data(self, market_data: dict) -> MarketEvent:
        # Debugging: Print keys if we suspect missing data
        # print(f"DEBUG DATA KEYS: {market_data.keys()}")
        
        # Polymarket sometimes stores prices as a JSON string, sometimes as a list
        raw_prices = market_data.get('outcomePrices')
        
        if raw_prices is None:
            # If price is missing, it's better to return None than a fake 50%
            print("   (Warning) 'outcomePrices' missing from API data.")
            return None

        # Parse the price
        try:
            # If it's a string like "['0.1', '0.9']", parse it
            if isinstance(raw_prices, str):
                prices = json.loads(raw_prices)
            else:
                prices = raw_prices

            prob = float(prices[0])
        except (ValueError, IndexError, TypeError):
            prob = 0.5

        return MarketEvent(
            event_name=market_data.get('question', 'Unknown Event'),
            source_name="Polymarket",
            probability=prob
        )