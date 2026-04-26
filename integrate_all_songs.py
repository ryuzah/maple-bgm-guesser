#!/usr/bin/env python3
"""
Script to integrate the complete MapleStory music database (1,308 songs)
into the BGM guessing game with proper formatting.
"""

import json
import requests
from datetime import datetime

def integrate_all_songs():
    """Download and integrate all MapleStory songs into the game."""
    
    print("Starting integration of complete MapleStory music database...")
    
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
    
    # Convert to our game's metadata format
    game_metadata = []
    
    for i, song in enumerate(all_songs, 1):
        # Extract song name
        song_name = song['metadata']['title'] if 'metadata' in song and 'title' in song['metadata'] else song['filename']
        
        # Extract region information
        region = "Unknown"
        if 'description' in song and song['description']:
            region = song['description']
        elif 'mark' in song and song['mark']:
            region = song['mark']
        
        # Get YouTube URL
        youtube_url = ""
        if 'youtube' in song and song['youtube']:
            youtube_url = f"https://www.youtube.com/watch?v={song['youtube']}"
        
        # Create entry in our game's format
        game_entry = {
            "id": i,
            "name": song_name,
            "regions": {
                "id": i,
                "town": region
            },
            "url": youtube_url
        }
        
        game_metadata.append(game_entry)
    
    # Create backup of original file
    backup_file = f"songs_metadata_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    try:
        with open('songs_metadata.json', 'r', encoding='utf-8') as f:
            original_data = f.read()
        
        with open(backup_file, 'w', encoding='utf-8') as f:
            f.write(original_data)
        
        print(f"Created backup: {backup_file}")
    except FileNotFoundError:
        print("No original songs_metadata.json found to backup")
    
    # Save the complete metadata
    with open('songs_metadata.json', 'w', encoding='utf-8') as f:
        json.dump(game_metadata, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully updated songs_metadata.json with {len(game_metadata)} songs")
    
    # Display statistics
    print("\n=== Integration Statistics ===")
    print(f"Total songs integrated: {len(game_metadata)}")
    
    # Count songs with YouTube URLs
    with_youtube = sum(1 for song in game_metadata if song['url'])
    print(f"Songs with YouTube URLs: {with_youtube}")
    
    # Count by client (region)
    client_counts = {}
    for song in all_songs:
        if 'source' in song and 'client' in song['source']:
            client = song['source']['client']
            client_counts[client] = client_counts.get(client, 0) + 1
    
    print("\nSongs by MapleStory region:")
    for client, count in sorted(client_counts.items()):
        print(f"  {client}: {count} songs")
    
    # Show sample songs
    print("\nSample integrated songs:")
    for i, song in enumerate(game_metadata[:5]):
        print(f"{i+1}. {song['name']} - {song['regions']['town']}")
        print(f"   YouTube: {song['url']}")
    
    print(f"\nIntegration complete! Your game now has {len(game_metadata)} MapleStory songs!")
    print("Note: You'll need to run the download script to get the audio files.")
    
    return game_metadata

if __name__ == "__main__":
    integrate_all_songs()
