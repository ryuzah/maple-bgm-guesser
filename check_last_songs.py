import json

with open('songs_metadata.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('Last 5 songs:')
for song in data[-5:]:
    tag_info = "(oldschool)" if 'tags' in song and 'oldschool' in song['tags'] else ""
    print(f"{song['id']}: {song['name']} - {song['regions']['town']} {tag_info}")
