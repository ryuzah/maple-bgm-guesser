#!/usr/bin/env python3
"""
Script to filter songs from specific regions and keep only:
- KMS (Korea)
- KMST (Korea Test Server) 
- GMS (Global)
- MSEA (Southeast Asia)

Remove songs from:
- CMST (China Test): 152 songs
- JMS (Japan): 95 songs
- CMS (China): 50 songs
- TMS (Taiwan): 46 songs
- ThMS (Thailand): 5 songs
- BMS (Brazil): 3 songs
- MSN (MapleStory N): 4 songs
- GMSC (Global Test): 2 songs
- TMST (Taiwan Test): 3 songs
"""

import json
import requests
from datetime import datetime

def filter_songs():
    """Filter songs to keep only KMS, KMST, GMS, and MSEA."""
    
    print("Filtering MapleStory songs by region...")
    
    # Regions to keep
    allowed_regions = {'KMS', 'KMST', 'GMS', 'MSEA'}
    
    # Regions to remove
    regions_to_remove = {
        'CMST', 'JMS', 'CMS', 'TMS', 'ThMS', 'BMS', 'MSN', 'GMSC', 'TMST'
    }
    
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
    
    # Filter songs by region
    filtered_songs = []
    removed_counts = {}
    kept_counts = {}
    
    for song in all_songs:
        if 'source' in song and 'client' in song['source']:
            client = song['source']['client']
            
            if client in allowed_regions:
                # Keep this song
                filtered_songs.append(song)
                kept_counts[client] = kept_counts.get(client, 0) + 1
            elif client in regions_to_remove:
                # Remove this song
                removed_counts[client] = removed_counts.get(client, 0) + 1
            else:
                # Unknown region, keep for safety
                filtered_songs.append(song)
                kept_counts[client] = kept_counts.get(client, 0) + 1
    
    print(f"\nFiltering Results:")
    print(f"Original total: {len(all_songs)} songs")
    print(f"Filtered total: {len(filtered_songs)} songs")
    print(f"Removed: {len(all_songs) - len(filtered_songs)} songs")
    
    print(f"\nSongs kept by region:")
    for region, count in sorted(kept_counts.items()):
        print(f"  {region}: {count} songs")
    
    print(f"\nSongs removed by region:")
    for region, count in sorted(removed_counts.items()):
        print(f"  {region}: {count} songs")
    
    # Convert to our game's metadata format
    game_metadata = []
    
    for i, song in enumerate(filtered_songs, 1):
        # Extract song name
        song_name = song['metadata']['title'] if 'metadata' in song and 'title' in song['metadata'] else song['filename']
        
        # Extract region information
        region = "Unknown"
        if 'mark' in song and song['mark']:
            region = song['mark']
        elif 'description' in song and song['description']:
            region = song['description']
        
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
    
    # Create backup of current file
    backup_file = f"songs_metadata_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    try:
        with open('songs_metadata.json', 'r', encoding='utf-8') as f:
            original_data = f.read()
        
        with open(backup_file, 'w', encoding='utf-8') as f:
            f.write(original_data)
        
        print(f"\nCreated backup: {backup_file}")
    except FileNotFoundError:
        print("No original songs_metadata.json found to backup")
    
    # Save the filtered metadata
    with open('songs_metadata.json', 'w', encoding='utf-8') as f:
        json.dump(game_metadata, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully updated songs_metadata.json with {len(game_metadata)} filtered songs")
    
    # Show sample songs
    print(f"\nSample filtered songs:")
    for i, song in enumerate(game_metadata[:5]):
        print(f"{i+1}. {song['name']} - {song['regions']['town']}")
    
    print(f"\nFiltering complete! Your game now has {len(game_metadata)} songs from KMS, KMST, GMS, and MSEA regions only!")
    
    return game_metadata

if __name__ == "__main__":
    filter_songs()
