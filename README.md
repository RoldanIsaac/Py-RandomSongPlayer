# Random Music Player 🎵

A simple Python script that randomly selects and plays a song from your music library.

## Features ✨

- Scans your entire music library (including subfolders)
- Randomly selects a song
- Plays the selected song using the default system player
- Supports MP3 files (easily extendable to other formats)

## Requirements 📋

- Python 3.x
- Windows OS (for `os.startfile()`)

## Installation & Setup ⚙️

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/random-music-player.git
   cd random-music-player

   ```

2. Configure your music library path:

Edit main.py and change the musicDir variable to point to your music folder:
musicDir = 'D:\Music\Music Library' # Change this to your music directory

## Usage 🎶

Simply run the script:

   ```bash
    python main.py

   ```

The script will:

- Scan your music library
- Randomly select a song
- Play it using your default media player

## File Structure 📂

   ```text
    random-music-player/
    ├── loadFolder.py # Folder scanning module
    ├── main.py # Main script
    └── README.md # This file

   ```

## Customization 🛠️

To support other file formats, modify the ext variable:

   ```python
    ext = '.mp3' # Can be changed to '.wav', '.flac', etc.

   ```

## Notes 📝

Currently Windows-only due to os.startfile()
For macOS/Linux support, consider replacing os.startfile() with:

   ```python
    os.system(f'open "{filepath}"') # macOS
    os.system(f'xdg-open "{filepath}"') # Linux

   ```

## License 📄

MIT License - Feel free to modify and distribute!


