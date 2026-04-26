#!/usr/bin/env python3
"""
Script to find and display the complete metadata for "Awakening of Old God" song
"""

import json
import requests

def find_awakening_old_god():
    """Find Awakening of Old God song and display its complete metadata."""
    
    print("Searching for 'Awakening of Old God' in MapleStory music database...")
    
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
    
    # Search for "Awakening of Old God"
    awakening_songs = []
    
    for song in all_songs:
        # Check in title, filename, or description
        title = song.get('metadata', {}).get('title', '').lower()
        filename = song.get('filename', '').lower()
        description = song.get('description', '').lower()
        
        if 'awakening of old god' in title or 'awakening of old god' in filename or 'awakening of old god' in description:
            awakening_songs.append(song)
    
    print(f"\nFound {len(awakening_songs)} songs matching 'Awakening of Old God':")
    
    for i, song in enumerate(awakening_songs, 1):
        print(f"\n=== Awakening of Old God Song #{i} ===")
        print(json.dumps(song, indent=2, ensure_ascii=False))
        print("-" * 50)

if __name__ == "__main__":
    find_awakening_old_god()
