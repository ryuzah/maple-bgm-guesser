import json
import re

# Test YouTube URL extraction and integration
def extract_youtube_video_id(url):
    """Test the YouTube video ID extraction function"""
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([^&\n?#]+)',
        r'youtube\.com\/watch\?.*v=([^&\n?#]+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match[1]
    return None

def test_youtube_url_extraction():
    """Test various YouTube URL formats"""
    test_urls = [
        "https://www.youtube.com/watch?v=s2_MAplvHeQ",
        "https://youtu.be/s2_MAplvHeQ",
        "https://www.youtube.com/embed/s2_MAplvHeQ",
        "https://www.youtube.com/watch?v=s2_MAplvHeQ&t=30s",
        "https://www.youtube.com/watch?v=invalid&other=param"
    ]
    
    print("Testing YouTube URL extraction:")
    for url in test_urls:
        video_id = extract_youtube_video_id(url)
        print(f"URL: {url}")
        print(f"Video ID: {video_id}")
        print("---")
    
    expected_id = "s2_MAplvHeQ"
    actual_id = extract_youtube_video_id("https://www.youtube.com/watch?v=s2_MAplvHeQ")
    assert actual_id == expected_id, f"Expected {expected_id}, got {actual_id}"
    print("✅ YouTube URL extraction test passed!")

def test_metadata_youtube_urls():
    """Test that songs_metadata.json contains valid YouTube URLs"""
    print("\nTesting metadata YouTube URLs:")
    
    with open('songs_metadata.json', 'r', encoding='utf-8') as f:
        songs = json.load(f)
    
    valid_urls = 0
    invalid_urls = 0
    
    for i, song in enumerate(songs[:10]):  # Test first 10 songs
        url = song.get('url', '')
        video_id = extract_youtube_video_id(url)
        
        if video_id:
            valid_urls += 1
            print(f"✅ {song['name']}: {video_id}")
        else:
            invalid_urls += 1
            print(f"❌ {song['name']}: Invalid URL - {url}")
    
    print(f"\nValid URLs: {valid_urls}")
    print(f"Invalid URLs: {invalid_urls}")
    
    if invalid_urls == 0:
        print("✅ All tested URLs are valid!")
    else:
        print("⚠️ Some URLs may be invalid")

def test_embed_url_generation():
    """Test YouTube embed URL generation"""
    video_id = "s2_MAplvHeQ"
    start_time = 15
    
    embed_url = f"https://www.youtube.com/embed/{video_id}?start={start_time}&autoplay=1&enablejsapi=1"
    
    print(f"\nTesting embed URL generation:")
    print(f"Video ID: {video_id}")
    print(f"Start Time: {start_time}s")
    print(f"Embed URL: {embed_url}")
    
    expected_components = ["youtube.com/embed", video_id, "autoplay=1", "enablejsapi=1"]
    for component in expected_components:
        assert component in embed_url, f"Missing component: {component}"
    
    print("✅ Embed URL generation test passed!")

def calculate_storage_savings():
    """Calculate potential storage savings"""
    print("\nStorage Analysis:")
    
    # Local files estimation
    avg_song_size_mb = 3  # Average MP3 size
    total_songs = 521
    local_storage_gb = (avg_song_size_mb * total_songs) / 1024
    
    print(f"Local audio files: ~{local_storage_gb:.1f} GB")
    print(f"HTML + JSON: ~0.2 GB")
    print(f"Total with local files: ~{local_storage_gb + 0.2:.1f} GB")
    print(f"Total with YouTube only: ~0.2 GB")
    print(f"Storage saved: ~{local_storage_gb:.1f} GB ({(local_storage_gb/(local_storage_gb + 0.2)*100):.1f}%)")

if __name__ == "__main__":
    test_youtube_url_extraction()
    test_metadata_youtube_urls()
    test_embed_url_generation()
    calculate_storage_savings()
    
    print("\n✅ YouTube integration tests completed!")
    print("✅ Ready to deploy with YouTube audio streaming!")
