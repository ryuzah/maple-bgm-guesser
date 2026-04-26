import json

# Load the metadata file
with open('songs_metadata.json', 'r', encoding='utf-8') as f:
    songs = json.load(f)

# Test filtering logic
print(f"Total songs in library: {len(songs)}")

# Count oldschool songs
oldschool_songs = [song for song in songs if 'tags' in song and 'oldschool' in song['tags']]
print(f"Oldschool songs: {len(oldschool_songs)}")

# Show some examples
print("\nSample oldschool songs:")
for song in oldschool_songs[:5]:
    print(f"  - {song['name']} - {song['regions']['town']}")

print("\nSample non-oldschool songs:")
non_oldschool = [song for song in songs if not ('tags' in song and 'oldschool' in song['tags'])]
for song in non_oldschool[:5]:
    print(f"  - {song['name']} - {song['regions']['town']}")

# Test filtering for different game modes
def filter_songs_by_mode(songs, game_mode):
    if game_mode == 'oldschool':
        return [song for song in songs if 'tags' in song and 'oldschool' in song['tags']]
    else:
        return songs

# Test both modes
all_songs = filter_songs_by_mode(songs, 'all')
oldschool_only = filter_songs_by_mode(songs, 'oldschool')

print(f"\nGame mode test results:")
print(f"All songs mode: {len(all_songs)} songs available")
print(f"Oldschool mode: {len(oldschool_only)} songs available")

# Verify the filtering works correctly
assert len(all_songs) == len(songs), "All songs mode should include all songs"
assert len(oldschool_only) == len(oldschool_songs), "Oldschool mode should only include oldschool songs"

print("\n✅ Game mode filtering test passed!")
