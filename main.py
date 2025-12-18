from src.fetcher import PolymarketFetcher

def main():
    fetcher = PolymarketFetcher()
    
    # Now we can mix IDs, Event Slugs, and Market Slugs!
    mixed_inputs = [
        "super-bowl-champion-2026-731",                                           # Numeric ID
        "democratic-presidential-nominee-2028", # Market Slug
        "cfb-mia-txam-2025-12-20"                             # Event Slug
    ]

    print("🚀 MarketOracle: Smart Analysis...\n")

    for item in mixed_inputs:
        print(f"🔍 Looking up: {item}...")
        event = fetcher.get_market(item) # <--- The new smart method
        
        if event:
            print(f"✅ Found: {event.event_name}")
            print(f"📊 Probability: {round(event.probability * 100, 1)}%\n")
        else:
            print(f"❌ Not found.\n")

if __name__ == "__main__":
    main()