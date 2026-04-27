# Maple BGM Guessing Game

A fun browser-based guessing game for MapleStory background music fans!

## Features

- **Two Difficulty Modes**:
  - **Easy Mode**: Guess the region/town name (e.g., "Ellinia")
  - **Hard Mode**: Guess the full song name with region (e.g., "Above the Treetops - Ellinia")

- **Flexible Game Length**: Choose between 5, 10, or 20 songs per round

- **Progressive Audio Clues**: Each song has 5 rounds with increasing audio duration:
  - Round 1: 1 second (5 points)
  - Round 2: 3 seconds (4 points)
  - Round 3: 5 seconds (3 points)
  - Round 4: 8 seconds (2 points)
  - Round 5: 10 seconds (1 point)

- **Smart Autocomplete**: Text input with intelligent suggestions based on difficulty mode

- **Score Tracking**: Current score and persistent high score storage

- **Modern UI**: Beautiful, responsive design with smooth animations

## Quick Start

### Option 1: Play Immediately (Demo Mode)

1. Open `index.html` in your web browser
2. The game will load with demo data and simulate audio playback
3. Select your preferred number of songs and difficulty
4. Start playing!

### Option 2: Full Audio Experience

To download all the actual MP3 files and have real audio playback:

1. **Install Dependencies**:
   ```bash
   pip install yt-dlp requests
   ```

2. **Download Songs**:
   ```bash
   python extract_songs.py
   ```
   This will:
   - Download all 120+ MapleStory BGM tracks from YouTube
   - Save them as MP3 files in the `bgm_files/` directory
   - Create `songs_metadata.json` with all song information

3. **Play the Game**:
   - Open `index.html` in your browser
   - Enjoy the full audio experience!

## Game Controls

- **Play Audio**: Click to play the current audio clip for the active round
- **Replay**: Replays the same audio clip after initial play
- **Submit Guess**: Submits your answer
- **Skip**: Skip the current song (0 points awarded)
- **Autocomplete**: Use arrow keys to navigate suggestions, Enter to select, Escape to close

## File Structure

```
maple-bgm-game/
├── index.html              # Main game interface
├── songs_metadata.json     # Song data (regions, names, URLs)
├── extract_songs.py        # Python script to download MP3s
├── bgm_files/              # Directory for downloaded MP3 files
└── README.md              # This file
```

## Technical Details

### Audio System

The game is designed to work with local MP3 files. When you run the download script:

- Each song is downloaded as: `"Song Name - Region.mp3"`
- Files are stored in the `bgm_files/` directory
- The game loads these files dynamically for playback

### Scoring System

- Correct answers earn points based on the round:
  - Round 1 (1s): 5 points
  - Round 2 (3s): 4 points  
  - Round 3 (5s): 3 points
  - Round 4 (8s): 2 points
  - Round 5 (10s): 1 point
- Incorrect or skipped answers: 0 points
- High scores are saved in browser's localStorage

### Difficulty Differences

**Easy Mode**:
- Autocomplete shows only region names
- Correct answer is just the region (e.g., "Henesys")
- Perfect for casual players or those less familiar with specific track names

**Hard Mode**:
- Autocomplete shows full song names with regions
- Correct answer includes both song name and region (e.g., "Floral Life - Henesys")
- Challenging for MapleStory veterans

## Browser Compatibility

- Modern browsers (Chrome, Firefox, Safari, Edge)
- Requires JavaScript enabled
- Responsive design works on desktop and mobile devices

## Troubleshooting

### Audio Not Playing
- Verify browser allows audio playback

### Songs Not Loading
- Make sure `songs_metadata.json` exists in the same directory as `index.html`
- Check browser console for any error messages

### Download Issues
- Some YouTube videos might be unavailable or region-locked
- The script will log any failed downloads but continue with others
- You can still play the game with partially downloaded songs

## Game Data

The game includes 120+ MapleStory BGM tracks from all major regions:

- **Starting Areas**: Maple Island, Lith Harbor
- **Victoria Island**: Perion, Ellinia, Henesys, Kerning City
- **Ossyria**: Orbis, El Nath, Aqua Road, Ludibrium
- **Masteria**: New Leaf City, Crimsonwood Keep
- **And many more!**

Each track includes metadata for accurate region identification and scoring.

Enjoy testing your MapleStory music knowledge! 🎵
