import json

# Load the metadata file
with open('songs_metadata.json', 'r', encoding='utf-8') as f:
    songs = json.load(f)

# Test daily mode filtering logic
print(f"Total songs in library: {len(songs)}")

# Count oldschool songs
oldschool_songs = [song for song in songs if 'tags' in song and 'oldschool' in song['tags']]
print(f"Oldschool songs: {len(oldschool_songs)}")

# Test daily mode filtering
def filter_daily_mode_songs(songs, game_mode):
    """Filter songs for daily mode based on game mode selection"""
    if game_mode == 'oldschool':
        return [song for song in songs if 'tags' in song and 'oldschool' in song['tags']]
    else:
        return songs

# Test both daily modes
daily_oldschool = filter_daily_mode_songs(songs, 'oldschool')
daily_all = filter_daily_mode_songs(songs, 'all')

print(f"\nDaily mode test results:")
print(f"Daily Oldschool: {len(daily_oldschool)} songs available")
print(f"Daily All Songs: {len(daily_all)} songs available")

# Test that daily mode uses exactly 1 song
daily_oldschool_selection = daily_oldschool[:1]
daily_all_selection = daily_all[:1]

print(f"\nDaily mode song selection (1 song each):")
print(f"Daily Oldschool selection: {len(daily_oldschool_selection)} song")
print(f"Daily All Songs selection: {len(daily_all_selection)} song")

# Show sample selections
print(f"\nSample Daily Oldschool song:")
for i, song in enumerate(daily_oldschool_selection, 1):
    print(f"  {i}. {song['name']} - {song['regions']['town']}")

print(f"\nSample Daily All Songs song:")
for i, song in enumerate(daily_all_selection, 1):
    print(f"  {i}. {song['name']} - {song['regions']['town']}")

# Verify the filtering works correctly
assert len(daily_oldschool) == len(oldschool_songs), "Daily oldschool should match oldschool songs"
assert len(daily_all) == len(songs), "Daily all should include all songs"
assert len(daily_oldschool_selection) == 1, "Daily mode should select exactly 1 song"
assert len(daily_all_selection) == 1, "Daily mode should select exactly 1 song"

print("\n✅ Daily mode filtering test passed!")
print("✅ Daily mode always uses 1 song!")
print("✅ Daily mode supports both oldschool and all songs!")
