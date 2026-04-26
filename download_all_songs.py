#!/usr/bin/env python3
"""
Download all songs from the updated songs_metadata.json file
"""

import json
import os
from yt_dlp import YoutubeDL
import time

def download_all_songs():
    """Download all songs from songs_metadata.json as MP3 files"""
    
    # Load songs from metadata file
    try:
        with open('songs_metadata.json', 'r', encoding='utf-8') as f:
            songs = json.load(f)
    except Exception as e:
        print(f"Error loading songs_metadata.json: {e}")
        return
    
    print(f"Found {len(songs)} songs to download")
    
    # Create directories
    os.makedirs("bgm_files", exist_ok=True)
    
    failed_downloads = []
    successful_downloads = []
    
    print("Starting download of MapleStory BGM files...")
    print("Note: This requires yt-dlp and optionally FFmpeg for MP3 conversion.")
    print("\nTo install yt-dlp: pip install yt-dlp")
    print("To install FFmpeg on Windows:")
    print("1. Go to: https://ffmpeg.org/download.html")
    print("2. Download 'ffmpeg-release-full.7z' for Windows")
    print("3. Extract and add ffmpeg.exe to your system PATH")
    print("4. Or use: choco install ffmpeg (if you have Chocolatey)")
    print()
    
    # Check if FFmpeg is available
    import subprocess
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
        ffmpeg_available = True
        print("✓ FFmpeg found - will convert to MP3")
    except (subprocess.CalledProcessError, FileNotFoundError):
        ffmpeg_available = False
        print("⚠ FFmpeg not found - will download as original format")
    
    print(f"\nDownloading {len(songs)} songs...\n")
    
    for i, song in enumerate(songs):
        print(f"[{i+1}/{len(songs)}] {song['name']} - {song['regions']['town']}")
        
        # Clean filename for this song
        clean_name = f"{song['name']} - {song['regions']['town']}"
        
        # Configure yt-dlp for this specific song
        if ffmpeg_available:
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': f'bgm_files/{clean_name}.%(ext)s',
                'quiet': True,
                'no_warnings': True,
            }
        else:
            # Download without conversion - will save as webm/m4a
            ydl_opts = {
                'format': 'bestaudio[ext=webm]/bestaudio[ext=m4a]/bestaudio/best',
                'outtmpl': f'bgm_files/{clean_name}.%(ext)s',
                'quiet': True,
                'no_warnings': True,
            }
        
        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([song['url']])
                print(f"  ✓ Downloaded successfully")
                successful_downloads.append(song)
                
        except Exception as e:
            error_msg = str(e)
            print(f"  ✗ Failed: {error_msg}")
            failed_downloads.append(song)
        
        # Small delay to be respectful
        time.sleep(0.5)
    
    print(f"\n" + "="*50)
    print(f"Download complete!")
    print(f"Successfully downloaded: {len(successful_downloads)}")
    print(f"Failed downloads: {len(failed_downloads)}")
    print(f"Files saved in: bgm_files/")
    
    if failed_downloads:
        print(f"\nFailed songs ({len(failed_downloads)}):")
        for song in failed_downloads[:10]:  # Show first 10 failures
            print(f"  - {song['name']} - {song['regions']['town']}")
        if len(failed_downloads) > 10:
            print(f"  ... and {len(failed_downloads) - 10} more")
    
    # Create a summary file
    summary = {
        'total_songs': len(songs),
        'successful': len(successful_downloads),
        'failed': len(failed_downloads),
        'ffmpeg_available': ffmpeg_available,
        'download_time': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    
    with open('download_summary.json', 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)
    
    print(f"\nDownload summary saved to: download_summary.json")

if __name__ == "__main__":
    download_all_songs()
