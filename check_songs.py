#!/usr/bin/env python3
"""
Check the current song count and details in the metadata file
"""

import json

def check_songs():
    try:
        with open('songs_metadata.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"Total songs: {len(data)}")
        print(f"First song: {data[0]['name']} - {data[0]['regions']['town']}")
        print(f"Last song: {data[-1]['name']} - {data[-1]['regions']['town']}")
        
        # Count unique towns
        towns = set()
        for song in data:
            towns.add(song['regions']['town'])
        print(f"Unique towns: {len(towns)}")
        
        return len(data)
    except Exception as e:
        print(f"Error: {e}")
        return 0

if __name__ == "__main__":
    check_songs()
