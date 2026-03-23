import requests
import random
import time
from datetime import datetime, timedelta

FIREBASE_URL = "https://games-rkoots-default-rtdb.firebaseio.com/scorecard.json"

GAMES = [
    {"id": "reaction-speed", "emoji": "⚡", "name": "Reaction Speed", "unit": "ms", "lower_better": True},
    {"id": "number-memory", "emoji": "🧠", "name": "Number Memory", "unit": "digits", "lower_better": False},
    {"id": "typing-speed", "emoji": "⌨️", "name": "Typing Speed", "unit": "WPM", "lower_better": False},
    {"id": "color-memory", "emoji": "🎨", "name": "Color Memory", "unit": "level", "lower_better": False},
    {"id": "sequence-memory", "emoji": "🔢", "name": "Sequence Memory", "unit": "level", "lower_better": False},
    {"id": "dhurandhar", "emoji": "🎯", "name": "Dhurandhar", "unit": "pts", "lower_better": False}
]

INDIAN_NAMES = [
    "Arjun Sharma", "Priya Patel", "Rohan Kumar", "Ananya Singh", "Vikram Reddy",
    "Sneha Gupta", "Aditya Mehta", "Kavya Iyer", "Rahul Verma", "Ishita Joshi"
]

AMERICAN_NAMES = [
    "James Wilson", "Emma Johnson", "Michael Brown", "Olivia Davis", "William Martinez",
    "Sophia Garcia", "Robert Anderson", "Ava Taylor", "David Thomas", "Isabella Moore"
]

ALL_NAMES = INDIAN_NAMES + AMERICAN_NAMES

def generate_score(game, player_skill):
    """Generate realistic scores based on game type and player skill (0-1)"""
    if game["id"] == "reaction-speed":
        base = 180 + (1 - player_skill) * 120
        return int(base + random.uniform(-30, 30))
    
    elif game["id"] == "number-memory":
        base = 3 + player_skill * 9
        return int(base + random.uniform(-1, 2))
    
    elif game["id"] == "typing-speed":
        base = 30 + player_skill * 90
        return int(base + random.uniform(-10, 10))
    
    elif game["id"] == "color-memory":
        base = 2 + player_skill * 13
        return int(base + random.uniform(-1, 2))
    
    elif game["id"] == "sequence-memory":
        base = 2 + player_skill * 13
        return int(base + random.uniform(-1, 2))
    
    elif game["id"] == "dhurandhar":
        base = 100 + player_skill * 900
        return int(base + random.uniform(-50, 100))
    
    return 100

def generate_test_data():
    """Generate test data for all games"""
    data = {}
    
    # Select 10 random players
    selected_players = random.sample(ALL_NAMES, 10)
    
    # Assign skill levels to players
    player_skills = {name: random.uniform(0.3, 0.95) for name in selected_players}
    
    for game in GAMES:
        game_id = game["id"]
        data[game_id] = {}
        
        print(f"\n📊 Generating data for {game['name']}...")
        
        for player_name in selected_players:
            skill = player_skills[player_name]
            
            # Generate 15 submissions per player
            for i in range(15):
                # Generate timestamp within last 30 days
                days_ago = random.randint(0, 30)
                hours_ago = random.randint(0, 23)
                timestamp = datetime.now() - timedelta(days=days_ago, hours=hours_ago)
                ts = int(timestamp.timestamp() * 1000)
                
                # Generate score with some variation
                score_variation = random.uniform(0.85, 1.15)
                adjusted_skill = skill * score_variation
                adjusted_skill = max(0.1, min(0.99, adjusted_skill))
                score = generate_score(game, adjusted_skill)
                
                # Create unique key
                entry_key = f"{player_name.replace(' ', '_')}_{ts}_{i}"
                
                data[game_id][entry_key] = {
                    "name": player_name,
                    "score": score,
                    "timestamp": ts
                }
            
            print(f"  ✓ {player_name}: 15 submissions")
    
    return data

def post_to_firebase(data):
    """Post data to Firebase"""
    print("\n🚀 Posting data to Firebase...")
    print(f"URL: {FIREBASE_URL}")
    
    try:
        # First, get existing data
        response = requests.get(FIREBASE_URL)
        existing_data = response.json() if response.status_code == 200 else {}
        
        if existing_data is None:
            existing_data = {}
        
        # Merge with new data
        for game_id, entries in data.items():
            if game_id not in existing_data:
                existing_data[game_id] = {}
            existing_data[game_id].update(entries)
        
        # Post merged data
        response = requests.put(FIREBASE_URL, json=existing_data)
        
        if response.status_code == 200:
            print("✅ Data successfully posted to Firebase!")
            
            # Count total entries
            total_entries = sum(len(entries) for entries in data.items())
            print(f"\n📈 Summary:")
            print(f"  • Games: {len(GAMES)}")
            print(f"  • Players: 10")
            print(f"  • New entries per game: ~150")
            print(f"  • Total new entries: {total_entries}")
            return True
        else:
            print(f"❌ Error: {response.status_code}")
            print(response.text)
            return False
            
    except Exception as e:
        print(f"❌ Exception: {str(e)}")
        return False

if __name__ == "__main__":
    print("🎮 RKoots Games Leaderboard - Test Data Generator")
    print("=" * 60)
    
    # Generate data
    test_data = generate_test_data()
    
    # Post to Firebase
    success = post_to_firebase(test_data)
    
    if success:
        print("\n✨ All done! Check your leaderboard at:")
        print("   https://rkoots.github.io/games/leaderboard/")
    else:
        print("\n⚠️ Failed to post data. Please check Firebase URL and permissions.")
