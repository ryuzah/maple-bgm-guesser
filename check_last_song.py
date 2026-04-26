import json

with open('songs_metadata.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('Last song:')
song = data[-1]
tag_info = "(oldschool)" if 'tags' in song and 'oldschool' in song['tags'] else ""
print(f"{song['id']}: {song['name']} - {song['regions']['town']} {tag_info}")
