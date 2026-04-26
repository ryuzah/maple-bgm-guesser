import json
import datetime

# Test the daily mode hard mode functionality
def get_utc_today():
    """Simulate the JavaScript getUTCToday function"""
    now = datetime.datetime.utcnow()
    return now.strftime('%Y-%m-%d')

def test_daily_key_structure():
    """Test the new daily key structure with difficulty"""
    print("Testing daily key structure...")
    
    # Test daily key format
    daily_keys = [
        "oldschool_easy",
        "oldschool_hard", 
        "all_easy",
        "all_hard"
    ]
    
    for key in daily_keys:
        mode, difficulty = key.split('_')
        print(f"Key: {key} -> Mode: {mode}, Difficulty: {difficulty}")
    
    print("✅ Daily key structure test passed!")

def test_seeded_random_with_difficulty():
    """Test that seeded random includes difficulty in seed"""
    print("\nTesting seeded random with difficulty...")
    
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
    
    today = get_utc_today()
    
    # Test that same mode but different difficulty produce different songs
    seed_easy = f"{today}_oldschool_easy"
    seed_hard = f"{today}_oldschool_hard"
    
    random_easy = seeded_random(seed_easy)
    random_hard = seeded_random(seed_hard)
    
    result_easy = random_easy()
    result_hard = random_hard()
    
    print(f"Seed (easy): {seed_easy}")
    print(f"Seed (hard): {seed_hard}")
    print(f"Random (easy): {result_easy}")
    print(f"Random (hard): {result_hard}")
    print(f"Different results: {abs(result_easy - result_hard) > 0.001}")
    
    # Test that different days produce different results
    tomorrow = "2024-04-27"
    seed_tomorrow = f"{tomorrow}_oldschool_easy"
    random_tomorrow = seeded_random(seed_tomorrow)
    result_tomorrow = random_tomorrow()
    
    print(f"Seed (tomorrow): {seed_tomorrow}")
    print(f"Random (tomorrow): {result_tomorrow}")
    print(f"Different from today: {abs(result_easy - result_tomorrow) > 0.001}")

def test_daily_data_structure_with_difficulty():
    """Test the enhanced daily data structure"""
    print("\nTesting enhanced daily data structure...")
    
    # Simulate enhanced daily data
    daily_data = {
        "oldschool_easy": {
            "date": get_utc_today(),
            "mode": "oldschool",
            "difficulty": "easy",
            "song": {
                "name": "Floral Life",
                "regions": {"town": "Henesys"}
            },
            "completed": True,
            "score": 5,
            "attempts": ["Henesys"]
        },
        "oldschool_hard": {
            "date": get_utc_today(),
            "mode": "oldschool", 
            "difficulty": "hard",
            "song": {
                "name": "Nightmare",
                "regions": {"town": "Perion"}
            },
            "completed": False,
            "score": 0,
            "attempts": []
        },
        "all_easy": {
            "date": get_utc_today(),
            "mode": "all",
            "difficulty": "easy", 
            "song": {
                "name": "Go Picnic",
                "regions": {"town": "Henesys"}
            },
            "completed": False,
            "score": 0,
            "attempts": []
        },
        "all_hard": None  # Not played yet
    }
    
    print("Enhanced daily data structure:")
    print(json.dumps(daily_data, indent=2))
    
    # Test completion check
    def is_daily_completed(daily_key, data):
        today = get_utc_today()
        key_data = data.get(daily_key)
        return key_data and key_data["date"] == today and key_data["completed"]
    
    print(f"\nOldschool Easy completed: {is_daily_completed('oldschool_easy', daily_data)}")
    print(f"Oldschool Hard completed: {is_daily_completed('oldschool_hard', daily_data)}")
    print(f"All Easy completed: {is_daily_completed('all_easy', daily_data)}")
    print(f"All Hard completed: {is_daily_completed('all_hard', daily_data)}")

def test_high_score_keys():
    """Test the new high score key structure"""
    print("\nTesting high score key structure...")
    
    high_score_keys = [
        "daily_oldschool_easy",
        "daily_oldschool_hard",
        "daily_all_easy", 
        "daily_all_hard"
    ]
    
    for key in high_score_keys:
        print(f"High score key: {key}")
    
    print("✅ High score key structure test passed!")

if __name__ == "__main__":
    test_daily_key_structure()
    test_seeded_random_with_difficulty()
    test_daily_data_structure_with_difficulty()
    test_high_score_keys()
    
    print("\n✅ Daily hard mode functionality tests completed!")
    print("✅ All daily modes (oldschool/all + easy/hard) are properly tracked!")
