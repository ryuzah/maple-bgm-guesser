import json
import requests

# Load current metadata
with open('songs_metadata.json', 'r', encoding='utf-8') as f:
    current_songs = json.load(f)

# Get current song names for comparison
current_song_names = {song['name'] for song in current_songs}

# All MapleWordle songs (from the website data)
maplewordle_songs = [
    {"name": "Above the Treetops", "town": "Lith Harbor"},
    {"name": "Beachway", "town": "Florina Beach"},
    {"name": "Nightmare", "town": "Perion"},
    {"name": "Highland Star", "town": "Perion"},
    {"name": "Ancient Remains", "town": "Perion"},
    {"name": "Castle Ruins", "town": "Perion"},
    {"name": "Water Way", "town": "Perion"},
    {"name": "Eregos", "town": "Perion"},
    {"name": "When the Morning Comes", "town": "Ellinia"},
    {"name": "Moonlight Shadow", "town": "Ellinia"},
    {"name": "Missing You", "town": "Ellinia"},
    {"name": "Floral Life", "town": "Henesys"},
    {"name": "Go Picnic", "town": "Henesys"},
    {"name": "Rest 'N Peace", "town": "Henesys"},
    {"name": "Cava Bien", "town": "Henesys"},
    {"name": "Blue Sky", "town": "Mushroom Castle"},
    {"name": "Bad Guys", "town": "Kerning City"},
    {"name": "Jungle Book", "town": "Kerning City"},
    {"name": "Subway", "town": "Kerning City"},
    {"name": "Secret Flower", "town": "Kerning City"},
    {"name": "Sleepywood", "town": "Sleepywood"},
    {"name": "Ancient Move", "town": "Sleepywood"},
    {"name": "Evil Eyes", "town": "Sleepywood"},
    {"name": "Nautilus", "town": "Nautilus Port"},
    {"name": "Interior of Nautilus", "town": "Nautilus Port"},
    {"name": "101 Building", "town": "Kerning Square"},
    {"name": "101 Building Field", "town": "Kerning Square"},
    {"name": "101 Building Subway", "town": "Kerning Square"},
    {"name": "Shinin' Harbor", "town": "Orbis"},
    {"name": "Upon the Sky", "town": "Orbis"},
    {"name": "Arab Pirate", "town": "Orbis"},
    {"name": "Come With Me", "town": "Orbis"},
    {"name": "Tower of a Goddess", "town": "Orbis"},
    {"name": "Plot of Pixie", "town": "Orbis"},
    {"name": "Snowy Village", "town": "El Nath"},
    {"name": "Warm Regard", "town": "El Nath"},
    {"name": "Wolf Woods", "town": "El Nath"},
    {"name": "Abandoned Mine", "town": "El Nath"},
    {"name": "Hell Gate", "town": "El Nath"},
    {"name": "Mine Quest", "town": "El Nath"},
    {"name": "Welcome to Hell", "town": "El Nath"},
    {"name": "Final Fight", "town": "El Nath"},
    {"name": "Aquarium", "town": "Aqua Road"},
    {"name": "Shining Sea", "town": "Aqua Road"},
    {"name": "Blue World", "town": "Aqua Road"},
    {"name": "Deep Sea", "town": "Aqua Road"},
    {"name": "Aqua Cave", "town": "Aqua Road"},
    {"name": "Fantastic Thinking", "town": "Ludibrium"},
    {"name": "Flying in a Blue Dream", "town": "Ludibrium"},
    {"name": "Funny Time Maker", "town": "Ludibrium"},
    {"name": "High Enough", "town": "Ludibrium"},
    {"name": "Waltz For Work", "town": "Ludibrium"},
    {"name": "Wherever You Are", "town": "Ludibrium"},
    {"name": "Bizzarre Tales", "town": "Ludibrium"},
    {"name": "The Grotesque Way", "town": "Ludibrium"},
    {"name": "Timeless", "town": "Ludibrium"},
    {"name": "Timeless (B)", "town": "Ludibrium"},
    {"name": "Fairy Tale", "town": "Ludibrium"},
    {"name": "Fairy Tale (Faster Version)", "town": "Ludibrium"},
    {"name": "Fantasia", "town": "Ludibrium"},
    {"name": "Dark Shadow", "town": "Ludibrium"},
    {"name": "They're Menacing You", "town": "Ludibrium"},
    {"name": "Time Attack", "town": "Ludibrium"},
    {"name": "Let's March", "town": "Omega Sector"},
    {"name": "Let's Hunt Aliens", "town": "Omega Sector"},
    {"name": "For the Glory", "town": "Omega Sector"},
    {"name": "Finding Forest", "town": "Omega Sector"},
    {"name": "Down Town", "town": "Korean Folk Town"},
    {"name": "Dark Mountain", "town": "Korean Folk Town"},
    {"name": "Leafre", "town": "Leafre"},
    {"name": "Minar's Dream", "town": "Leafre"},
    {"name": "Ancient Forest", "town": "Leafre"},
    {"name": "Dragon Load", "town": "Leafre"},
    {"name": "Dragon's Nest", "town": "Leafre"},
    {"name": "Cave of Horntail", "town": "Leafre"},
    {"name": "Horntail", "town": "Leafre"},
    {"name": "Dragon Rider", "town": "Leafre"},
    {"name": "Mureung Hill", "town": "Mu Lung"},
    {"name": "Mureung Forest", "town": "Mu Lung"},
    {"name": "Mu Lung Raid 1", "town": "Mu Lung"},
    {"name": "Mu Lung Raid 2", "town": "Mu Lung"},
    {"name": "Mu Lung Raid 3", "town": "Mu Lung"},
    {"name": "Mu Lung Raid 4", "town": "Mu Lung"},
    {"name": "White Herb", "town": "Herb Town"},
    {"name": "Pirate", "town": "Herb Town"},
    {"name": "Ariant", "town": "Ariant"},
    {"name": "Hot Desert", "town": "Ariant"},
    {"name": "Fight Sand", "town": "Ariant"},
    {"name": "Sunset Desert", "town": "Ariant"},
    {"name": "Dispute", "town": "Magatia"},
    {"name": "Temple of Time", "town": "Temple of Time"},
    {"name": "Rememberance", "town": "Temple of Time"},
    {"name": "Repentance", "town": "Temple of Time"},
    {"name": "Forgetfulness", "town": "Temple of Time"},
    {"name": "Dusk of God", "town": "Temple of Time"},
    {"name": "Fighting Pink Bean", "town": "Temple of Time"},
    {"name": "Kamuna", "town": "Neo City"},
    {"name": "Park", "town": "Neo City"},
    {"name": "Odaiba", "town": "Neo City"},
    {"name": "Akihabara", "town": "Neo City"},
    {"name": "Office", "town": "Neo City"},
    {"name": "Tokyo Sky", "town": "Neo City"},
    {"name": "New Leaf City - Town", "town": "New Leaf City"},
    {"name": "New Leaf City - Hunt", "town": "New Leaf City"},
    {"name": "New Leaf City - Upbeat", "town": "New Leaf City"},
    {"name": "Phantom Forest (Original)", "town": "Crimsonwood Keep"},
    {"name": "Crimsonwood Keep", "town": "Crimsonwood Keep"},
    {"name": "Bigfoot", "town": "Crimsonwood Keep"},
    {"name": "Crimsonwood Party Quest", "town": "Crimsonwood Keep"},
    {"name": "Grandmaster's Gauntlet", "town": "Crimsonwood Keep"},
    {"name": "Crimsonwood Keep Interior", "town": "Crimsonwood Keep"},
    {"name": "Courtyard", "town": "Crimsonwood Keep"},
    {"name": "Haunted House", "town": "Haunted House"},
    {"name": "CBD Town", "town": "Singapore"},
    {"name": "CBD Field", "town": "Singapore"},
    {"name": "Boat Quay Town", "town": "Singapore"},
    {"name": "Boat Quay Field", "town": "Singapore"},
    {"name": "Ghost Ship", "town": "Singapore"},
    {"name": "Ulu Field", "town": "Singapore"},
    {"name": "Kuala Lumpur", "town": "Malaysia"},
    {"name": "Highland", "town": "Malaysia"},
    {"name": "Feeling", "town": "Zipangu"},
    {"name": "Bizarre Forest", "town": "Zipangu"},
    {"name": "Castle Trap", "town": "Zipangu"},
    {"name": "Castle Outside", "town": "Zipangu"},
    {"name": "Castle Inside", "town": "Zipangu"},
    {"name": "Castle Boss", "town": "Zipangu"},
    {"name": "Yume", "town": "Showa Town"},
    {"name": "Bathroom", "town": "Showa Town"},
    {"name": "Battlefield", "town": "Showa Town"},
    {"name": "Golden Temple Town", "town": "Golden Temple"},
    {"name": "Golden Temple Field", "town": "Golden Temple"},
    {"name": "Golden Temple Dungeon", "town": "Golden Temple"},
    {"name": "Elin Forest", "town": "Ellin Forest"},
    {"name": "Poison Forest", "town": "Ellin Forest"},
    {"name": "First Step Master", "town": "Maple Island"},
    {"name": "Queen's Garden", "town": "Ereve"},
    {"name": "Raindrop Flower", "town": "Ereve"},
    {"name": "Drill Hall", "town": "Ereve"},
    {"name": "Crystal Cave", "town": "Rien"},
    {"name": "Rien Village", "town": "Rien"},
    {"name": "Snow Drop", "town": "Rien"},
    {"name": "Bamboo Gym", "town": "Rien"},
    {"name": "Amoria", "town": "Amoria"},
    {"name": "Cathedral", "town": "Amoria"},
    {"name": "Chapel", "town": "Amoria"},
    {"name": "Amorian Challenge", "town": "Amoria"}
]

# Find missing songs
missing_songs = [song for song in maplewordle_songs if song["name"] not in current_song_names]

print(f"Found {len(missing_songs)} missing songs from MapleWordle:")

# Fetch original data to get URLs and other metadata
print("Fetching original BGM data...")
try:
    response = requests.get("https://raw.githubusercontent.com/maplestory-music/maplebgm-db/prod/bgm.min.json")
    original_data = response.json()
    print(f"Loaded {len(original_data)} songs from original database")
except Exception as e:
    print(f"Error fetching original data: {e}")
    original_data = []

# Create a lookup for original data
original_lookup = {song['metadata']['title']: song for song in original_data}

# Get next ID for new songs
max_id = max(song['id'] for song in current_songs) if current_songs else 0
next_id = max_id + 1

# Add missing songs
added_count = 0
for song in missing_songs:
    song_name = song["name"]
    town = song["town"]
    
    # Try to find in original data
    original_song = original_lookup.get(song_name)
    
    if original_song:
        url = f"https://www.youtube.com/watch?v={original_song['youtube']}"
        print(f"✓ Adding: {song_name} - {town}")
    else:
        # Fallback - create entry without URL
        url = ""
        print(f"⚠ Adding: {song_name} - {town} (no URL found)")
    
    new_song = {
        "id": next_id,
        "name": song_name,
        "regions": {
            "id": next_id,
            "town": town
        },
        "url": url,
        "tags": ["oldschool"]
    }
    
    current_songs.append(new_song)
    next_id += 1
    added_count += 1

# Save updated metadata
with open('songs_metadata.json', 'w', encoding='utf-8') as f:
    json.dump(current_songs, f, indent=2, ensure_ascii=False)

print(f"\n✅ Added {added_count} new oldschool songs!")
print(f"Total songs in metadata: {len(current_songs)}")

if added_count > 0:
    print("\nNew songs added:")
    for song in missing_songs:
        print(f"  - {song['name']} - {song['town']}")
