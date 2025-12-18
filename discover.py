import requests

def discover_markets():
    # We fetch the top 10 active events, sorted by volume
    url = "https://gamma-api.polymarket.com/events"
    params = {
        "limit": 10,
        "active": "true",
        "closed": "false",
        "order": "volume",
        "ascending": "false"
    }
    
    print("📡 Connecting to Polymarket API...")
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        events = response.json()
        print(f"\n✅ Found {len(events)} Trending Events:\n")
        print(f"{'EVENT NAME':<50} | {'SLUG (Copy This!)'}")
        print("-" * 85)
        
        for event in events:
            title = event.get('title', 'Unknown')[:45]
            slug = event.get('slug', 'N/A')
            print(f"{title:<50} | {slug}")
            
    else:
        print(f"❌ Error: {response.status_code}")

if __name__ == "__main__":
    discover_markets()