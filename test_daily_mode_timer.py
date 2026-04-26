import json
import datetime

# Test the daily mode timer and date logic
def get_utc_today():
    """Simulate the JavaScript getUTCToday function"""
    now = datetime.datetime.utcnow()
    return now.strftime('%Y-%m-%d')

def test_utc_date_logic():
    print("Testing UTC date logic...")
    today = get_utc_today()
    print(f"Today (UTC): {today}")
    
    # Test time until midnight calculation
    now = datetime.datetime.utcnow()
    tomorrow = datetime.datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    tomorrow += datetime.timedelta(days=1)
    
    diff = tomorrow - now
    hours = diff.seconds // 3600
    minutes = (diff.seconds % 3600) // 60
    seconds = diff.seconds % 60
    
    print(f"Time until midnight UTC: {hours:02d}:{minutes:02d}:{seconds:02d}")
    print(f"Total seconds until midnight: {diff.total_seconds()}")

def test_seeded_random():
    """Test the seeded random function logic"""
    print("\nTesting seeded random logic...")
    
    def seeded_random(seed):
        # Simulate the JavaScript seeded random
        hash_val = 0
        for i, char in enumerate(seed):
            char_code = ord(char)
            hash_val = ((hash_val << 5) - hash_val) + char_code
            hash_val = hash_val & hash_val  # Convert to 32bit integer
        
        def random_func():
            nonlocal hash_val
            hash_val = ((hash_val + 0x6D2B79F5) * 0x5BD1E995) & 0xFFFFFFFF
            return (hash_val >> 16) / 0xFFFFFFFF  # Simplified version
        return random_func
    
    # Test that same seed produces same result
    seed = "2024-04-26_oldschool"
    random1 = seeded_random(seed)
    random2 = seeded_random(seed)
    
    result1 = random1()
    result2 = random2()
    
    print(f"Seed: {seed}")
    print(f"Random 1: {result1}")
    print(f"Random 2: {result2}")
    print(f"Same results: {abs(result1 - result2) < 0.001}")
    
    # Test different seeds produce different results
    seed2 = "2024-04-26_all"
    random3 = seeded_random(seed2)
    result3 = random3()
    
    print(f"Seed 2: {seed2}")
    print(f"Random 3: {result3}")
    print(f"Different from first: {abs(result1 - result3) > 0.001}")

def test_daily_data_structure():
    """Test the daily data structure"""
    print("\nTesting daily data structure...")
    
    # Simulate daily data
    daily_data = {
        "oldschool": {
            "date": get_utc_today(),
            "song": {
                "name": "Floral Life",
                "regions": {"town": "Henesys"}
            },
            "completed": False,
            "score": 0,
            "attempts": []
        },
        "all": {
            "date": get_utc_today(),
            "song": {
                "name": "Nightmare",
                "regions": {"town": "Perion"}
            },
            "completed": True,
            "score": 5,
            "attempts": ["Henesys", "Perion"]
        }
    }
    
    print("Daily data structure:")
    print(json.dumps(daily_data, indent=2))
    
    # Test completion check
    def is_daily_completed(mode, data):
        today = get_utc_today()
        mode_data = data.get(mode)
        return mode_data and mode_data["date"] == today and mode_data["completed"]
    
    print(f"\nOldschool completed: {is_daily_completed('oldschool', daily_data)}")
    print(f"All completed: {is_daily_completed('all', daily_data)}")

if __name__ == "__main__":
    test_utc_date_logic()
    test_seeded_random()
    test_daily_data_structure()
    
    print("\n✅ Daily mode timer and logic tests completed!")
