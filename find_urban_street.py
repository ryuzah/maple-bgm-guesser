#!/usr/bin/env python3
"""
Script to find and display the complete metadata for "Urban Street" song
"""

import json
import requests

def find_urban_street():
    """Find Urban Street song and display its complete metadata."""
    
    print("Searching for 'Urban Street' in MapleStory music database...")
    
    # Fetch the complete data from the MapleStory music database
    url = "https://raw.githubusercontent.com/maplestory-music/maplebgm-db/prod/bgm.min.json"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        all_songs = response.json()
        print(f"Successfully fetched {len(all_songs)} songs from database")
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return
    
    # Search for "Urban Street"
    urban_street_songs = []
    
    for song in all_songs:
        # Check in title, filename, or description
        title = song.get('metadata', {}).get('title', '').lower()
        filename = song.get('filename', '').lower()
        description = song.get('description', '').lower()
        
        if 'urban street' in title or 'urban street' in filename or 'urban street' in description:
            urban_street_songs.append(song)
    
    print(f"\nFound {len(urban_street_songs)} songs matching 'Urban Street':")
    
    for i, song in enumerate(urban_street_songs, 1):
        print(f"\n=== Urban Street Song #{i} ===")
        print(json.dumps(song, indent=2, ensure_ascii=False))
        print("-" * 50)

if __name__ == "__main__":
    find_urban_street()
