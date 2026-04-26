import json
import re
import requests
import os
from yt_dlp import YoutubeDL
import time

def extract_song_data():
    """Extract song data from the website content"""
    # The JSON data was found in the HTML content
    songs_data = [
        {"id": 1, "name": "Above the Treetops", "url": "https://youtu.be/F6LIFBVhObQ", "regions": {"id": 1, "town": "Lith Harbor"}},
        {"id": 2, "name": "Beachway", "url": "https://youtu.be/9VqPnUL9Qvs", "regions": {"id": 2, "town": "Florina Beach"}},
        {"id": 3, "name": "Nightmare", "url": "https://youtu.be/9lwOsX763N0", "regions": {"id": 3, "town": "Perion"}},
        {"id": 4, "name": "Highland Star", "url": "https://youtu.be/DIuiKBGxPLA", "regions": {"id": 3, "town": "Perion"}},
        {"id": 5, "name": "Ancient Remains", "url": "https://youtu.be/fdoT7nTWMO8", "regions": {"id": 3, "town": "Perion"}},
        {"id": 6, "name": "Castle Ruins", "url": "https://youtu.be/xeks7rE2m0o", "regions": {"id": 3, "town": "Perion"}},
        {"id": 7, "name": "Water Way", "url": "https://youtu.be/Su6P7juLavE", "regions": {"id": 3, "town": "Perion"}},
        {"id": 8, "name": "Eregos", "url": "https://youtu.be/rNnYpo9-cRw", "regions": {"id": 3, "town": "Perion"}},
        {"id": 9, "name": "When the Morning Comes", "url": "https://youtu.be/gfgBDs8z6WE", "regions": {"id": 4, "town": "Ellinia"}},
        {"id": 10, "name": "Moonlight Shadow", "url": "https://youtu.be/XYtHWyrVm30", "regions": {"id": 4, "town": "Ellinia"}},
        {"id": 11, "name": "Missing You", "url": "https://youtu.be/2NoF8PHQJqQ", "regions": {"id": 4, "town": "Ellinia"}},
        {"id": 12, "name": "Floral Life", "url": "https://youtu.be/s2_MAplvHeQ", "regions": {"id": 5, "town": "Henesys"}},
        {"id": 13, "name": "Go Picnic", "url": "https://youtu.be/WUuawkZR0s0", "regions": {"id": 5, "town": "Henesys"}},
        {"id": 14, "name": "Rest 'N Peace", "url": "https://youtu.be/SQRqz1D3Xm8", "regions": {"id": 5, "town": "Henesys"}},
        {"id": 15, "name": "Cava Bien", "url": "https://youtu.be/ddd2MInZXUU", "regions": {"id": 5, "town": "Henesys"}},
        {"id": 20, "name": "Blue Sky", "url": "https://youtu.be/ClLLtA3naSo", "regions": {"id": 6, "town": "Mushroom Castle"}},
        {"id": 21, "name": "Bad Guys", "url": "https://youtu.be/uv8QObpL2EY", "regions": {"id": 7, "town": "Kerning City"}},
        {"id": 22, "name": "Jungle Book", "url": "https://youtu.be/YYTuDFsvZNU", "regions": {"id": 7, "town": "Kerning City"}},
        {"id": 23, "name": "Subway", "url": "https://youtu.be/J1YTQvtmsjg", "regions": {"id": 7, "town": "Kerning City"}},
        {"id": 152, "name": "Secret Flower", "url": "https://youtu.be/C0xN8QcxqXk", "regions": {"id": 7, "town": "Kerning City"}},
        {"id": 24, "name": "Sleepywood", "url": "https://youtu.be/tWCWIhA3XQw", "regions": {"id": 8, "town": "Sleepywood"}},
        {"id": 25, "name": "Ancient Move", "url": "https://youtu.be/w9HagZ099c0", "regions": {"id": 8, "town": "Sleepywood"}},
        {"id": 26, "name": "Evil Eyes", "url": "https://youtu.be/N49FmJJnfy0", "regions": {"id": 8, "town": "Sleepywood"}},
        {"id": 27, "name": "Nautilus", "url": "https://youtu.be/iZaVKkfuD6s", "regions": {"id": 9, "town": "Nautilus Port"}},
        {"id": 28, "name": "Interior of Nautilus", "url": "https://youtu.be/eZ8LtJlzvyU", "regions": {"id": 9, "town": "Nautilus Port"}},
        {"id": 29, "name": "101 Building", "url": "https://youtu.be/_0qKfYQG7Rs", "regions": {"id": 10, "town": "Kerning Square"}},
        {"id": 30, "name": "101 Building Field", "url": "https://youtu.be/hKYODtn_P84", "regions": {"id": 10, "town": "Kerning Square"}},
        {"id": 31, "name": "101 Building Subway", "url": "https://youtu.be/iRxal9QpFb8", "regions": {"id": 10, "town": "Kerning Square"}},
        {"id": 32, "name": "Shinin' Harbor", "url": "https://youtu.be/DThWMbPZXy8", "regions": {"id": 11, "town": "Orbis"}},
        {"id": 33, "name": "Upon the Sky", "url": "https://youtu.be/fTYJEdEcTbA", "regions": {"id": 11, "town": "Orbis"}},
        {"id": 34, "name": "Arab Pirate", "url": "https://youtu.be/PZLLGX6VNgU", "regions": {"id": 11, "town": "Orbis"}},
        {"id": 35, "name": "Come With Me", "url": "https://youtu.be/sNCwJu5Buz0", "regions": {"id": 11, "town": "Orbis"}},
        {"id": 36, "name": "Tower of a Goddess", "url": "https://youtu.be/UEByqQPt2is", "regions": {"id": 11, "town": "Orbis"}},
        {"id": 38, "name": "Plot of Pixie", "url": "https://youtu.be/znPiUenHhP4", "regions": {"id": 11, "town": "Orbis"}},
        {"id": 39, "name": "Snowy Village", "url": "https://youtu.be/X6X7U5V9Obk", "regions": {"id": 12, "town": "El Nath"}},
        {"id": 40, "name": "Warm Regard", "url": "https://youtu.be/MBmPOY2PA2Q", "regions": {"id": 12, "town": "El Nath"}},
        {"id": 41, "name": "Wolf Woods", "url": "https://youtu.be/1MPBnVU8_I4", "regions": {"id": 12, "town": "El Nath"}},
        {"id": 42, "name": "Abandoned Mine", "url": "https://youtu.be/WmHOENuKkmk", "regions": {"id": 12, "town": "El Nath"}},
        {"id": 43, "name": "Hell Gate", "url": "https://youtu.be/923LpjaA9Ps", "regions": {"id": 12, "town": "El Nath"}},
        {"id": 44, "name": "Mine Quest", "url": "https://youtu.be/8LaAGZ5kxvk", "regions": {"id": 12, "town": "El Nath"}},
        {"id": 45, "name": "Welcome to Hell", "url": "https://youtu.be/3EJFx4emHyk", "regions": {"id": 12, "town": "El Nath"}},
        {"id": 96, "name": "Final Fight", "url": "https://youtu.be/rEtDrkAYs68", "regions": {"id": 12, "town": "El Nath"}},
        {"id": 46, "name": "Aquarium", "url": "https://youtu.be/qtw0sIBLjrw", "regions": {"id": 13, "town": "Aqua Road"}},
        {"id": 47, "name": "Shining Sea", "url": "https://youtu.be/3jdRxzy3K9s", "regions": {"id": 13, "town": "Aqua Road"}},
        {"id": 48, "name": "Blue World", "url": "https://youtu.be/EnHRl2Wnabk", "regions": {"id": 13, "town": "Aqua Road"}},
        {"id": 49, "name": "Deep Sea", "url": "https://youtu.be/qc5Qqw7ABAU", "regions": {"id": 13, "town": "Aqua Road"}},
        {"id": 50, "name": "Aqua Cave", "url": "https://youtu.be/ctsqJ-Xl9_0", "regions": {"id": 13, "town": "Aqua Road"}},
        {"id": 51, "name": "Fantastic Thinking", "url": "https://youtu.be/49AZqVhXVeU", "regions": {"id": 14, "town": "Ludibrium"}},
        {"id": 52, "name": "Flying in a Blue Dream", "url": "https://youtu.be/UywGQsCoj8c", "regions": {"id": 14, "town": "Ludibrium"}},
        {"id": 53, "name": "Funny Time Maker", "url": "https://youtu.be/JSPCrPrepRE", "regions": {"id": 14, "town": "Ludibrium"}},
        {"id": 54, "name": "High Enough", "url": "https://youtu.be/iqWeh-dkwu4", "regions": {"id": 14, "town": "Ludibrium"}},
        {"id": 55, "name": "Waltz For Work", "url": "https://youtu.be/CNRFWEhv_Dw", "regions": {"id": 14, "town": "Ludibrium"}},
        {"id": 56, "name": "Wherever You Are", "url": "https://youtu.be/iHbjhiWic0U", "regions": {"id": 14, "town": "Ludibrium"}},
        {"id": 57, "name": "Bizzarre Tales", "url": "https://youtu.be/v187PexfsFM", "regions": {"id": 14, "town": "Ludibrium"}},
        {"id": 58, "name": "The Grotesque Way", "url": "https://youtu.be/5Uu68ZwkzrM", "regions": {"id": 14, "town": "Ludibrium"}},
        {"id": 59, "name": "Timeless", "url": "https://youtu.be/95a3-2TsrrA", "regions": {"id": 14, "town": "Ludibrium"}},
        {"id": 60, "name": "Timeless (B)", "url": "https://youtu.be/PmuoAR2ce3o", "regions": {"id": 14, "town": "Ludibrium"}},
        {"id": 61, "name": "Fairy Tale", "url": "https://youtu.be/0_PTb2pxygU", "regions": {"id": 14, "town": "Ludibrium"}},
        {"id": 62, "name": "Fairy Tale (Faster Version)", "url": "https://youtu.be/7PO-m2atU2U", "regions": {"id": 14, "town": "Ludibrium"}},
        {"id": 63, "name": "Fantasia", "url": "https://youtu.be/v-GtLObPoto", "regions": {"id": 14, "town": "Ludibrium"}},
        {"id": 64, "name": "Dark Shadow", "url": "https://youtu.be/wWB1hTbtoNQ", "regions": {"id": 14, "town": "Ludibrium"}},
        {"id": 65, "name": "They're Menacing You", "url": "https://youtu.be/hYVoxcVK0ns", "regions": {"id": 14, "town": "Ludibrium"}},
        {"id": 116, "name": "Time Attack", "url": "https://youtu.be/AiaV9gA3i10", "regions": {"id": 14, "town": "Ludibrium"}},
        {"id": 66, "name": "Let's March", "url": "https://youtu.be/LxQt8EVhBOs", "regions": {"id": 15, "town": "Omega Sector"}},
        {"id": 67, "name": "Let's Hunt Aliens", "url": "https://youtu.be/pZ6Fuv6BLx4", "regions": {"id": 15, "town": "Omega Sector"}},
        {"id": 68, "name": "For the Glory", "url": "https://youtu.be/aSTjTjakW8s", "regions": {"id": 15, "town": "Omega Sector"}},
        {"id": 69, "name": "Finding Forest", "url": "https://youtu.be/dT0laG5urcc", "regions": {"id": 15, "town": "Omega Sector"}},
        {"id": 70, "name": "Down Town", "url": "https://youtu.be/KK_IjvtszTA", "regions": {"id": 16, "town": "Korean Folk Town"}},
        {"id": 71, "name": "Dark Mountain", "url": "https://youtu.be/YUeCX11El2s", "regions": {"id": 16, "town": "Korean Folk Town"}},
        {"id": 72, "name": "Leafre", "url": "https://youtu.be/theIdIhZzVE", "regions": {"id": 17, "town": "Leafre"}},
        {"id": 73, "name": "Minar's Dream", "url": "https://youtu.be/07a-UZLcxhM", "regions": {"id": 17, "town": "Leafre"}},
        {"id": 74, "name": "Ancient Forest", "url": "https://youtu.be/pWi9HXGWn2k", "regions": {"id": 17, "town": "Leafre"}},
        {"id": 75, "name": "Dragon Load", "url": "https://youtu.be/z3jhg8KffPI", "regions": {"id": 17, "town": "Leafre"}},
        {"id": 76, "name": "Dragon's Nest", "url": "https://youtu.be/Dsis2wyHQD0", "regions": {"id": 17, "town": "Leafre"}},
        {"id": 77, "name": "Cave of Horntail", "url": "https://youtu.be/Lo59n_tMGSM", "regions": {"id": 17, "town": "Leafre"}},
        {"id": 97, "name": "Horntail", "url": "https://youtu.be/WnLrTMmnyBc", "regions": {"id": 17, "town": "Leafre"}},
        {"id": 139, "name": "Dragon Rider", "url": "https://youtu.be/s6zoD2gnYrA", "regions": {"id": 17, "town": "Leafre"}},
        {"id": 78, "name": "Mureung Hill", "url": "https://youtu.be/2VMCpGe9MGc", "regions": {"id": 18, "town": "Mu Lung"}},
        {"id": 79, "name": "Mureung Forest", "url": "https://youtu.be/OweBGLQHWaA", "regions": {"id": 18, "town": "Mu Lung"}},
        {"id": 80, "name": "Mu Lung Raid 1", "url": "https://youtu.be/bqR0o6TkkQk", "regions": {"id": 18, "town": "Mu Lung"}},
        {"id": 81, "name": "Mu Lung Raid 2", "url": "https://youtu.be/cypwlFD2TE4", "regions": {"id": 18, "town": "Mu Lung"}},
        {"id": 82, "name": "Mu Lung Raid 3", "url": "https://youtu.be/9SKZBsjUdAg", "regions": {"id": 18, "town": "Mu Lung"}},
        {"id": 83, "name": "Mu Lung Raid 4", "url": "https://youtu.be/44UN_MwwAEg", "regions": {"id": 18, "town": "Mu Lung"}},
        {"id": 84, "name": "White Herb", "url": "https://youtu.be/59oze7IkQ10", "regions": {"id": 19, "town": "Herb Town"}},
        {"id": 85, "name": "Pirate", "url": "https://youtu.be/bI9xLsAjeJk", "regions": {"id": 19, "town": "Herb Town"}},
        {"id": 86, "name": "Ariant", "url": "https://youtu.be/w1RgDSoOajw", "regions": {"id": 20, "town": "Ariant"}},
        {"id": 87, "name": "Hot Desert", "url": "https://youtu.be/q9swmo6309U", "regions": {"id": 20, "town": "Ariant"}},
        {"id": 88, "name": "Fight Sand", "url": "https://youtu.be/RQ35yqS4XZg", "regions": {"id": 20, "town": "Ariant"}},
        {"id": 90, "name": "Sunset Desert", "url": "https://youtu.be/L9CYYgoZVAo", "regions": {"id": 20, "town": "Ariant"}},
        {"id": 89, "name": "Dispute", "url": "https://youtu.be/5FDFLwPw0bU", "regions": {"id": 21, "town": "Magatia"}},
        {"id": 91, "name": "Temple of Time", "url": "https://youtu.be/6uCaEDM-Kf8", "regions": {"id": 22, "town": "Temple of Time"}},
        {"id": 92, "name": "Rememberance", "url": "https://youtu.be/TpKE4mKFSZY", "regions": {"id": 22, "town": "Temple of Time"}},
        {"id": 93, "name": "Repentance", "url": "https://youtu.be/3loq0xBsi7o", "regions": {"id": 22, "town": "Temple of Time"}},
        {"id": 94, "name": "Forgetfulness", "url": "https://youtu.be/mPdotLdAe7k", "regions": {"id": 22, "town": "Temple of Time"}},
        {"id": 95, "name": "Dusk of God", "url": "https://youtu.be/c851KzZNXkg", "regions": {"id": 22, "town": "Temple of Time"}},
        {"id": 98, "name": "Fighting Pink Bean", "url": "https://youtu.be/Mt8ZlyYA4GI", "regions": {"id": 22, "town": "Temple of Time"}},
        {"id": 99, "name": "Kamuna", "url": "https://youtu.be/BB1l4zunOVU", "regions": {"id": 23, "town": "Neo City"}},
        {"id": 100, "name": "Park", "url": "https://youtu.be/HDsv0jH1RzI", "regions": {"id": 23, "town": "Neo City"}},
        {"id": 101, "name": "Odaiba", "url": "https://youtu.be/KO8911CzgMU", "regions": {"id": 23, "town": "Neo City"}},
        {"id": 102, "name": "Akihabara", "url": "https://youtu.be/47hrhA3OqkU", "regions": {"id": 23, "town": "Neo City"}},
        {"id": 103, "name": "Office", "url": "https://youtu.be/nxtdTBejXRY", "regions": {"id": 23, "town": "Neo City"}},
        {"id": 104, "name": "Tokyo Sky", "url": "https://youtu.be/MVCmEQSeZak", "regions": {"id": 23, "town": "Neo City"}},
        {"id": 105, "name": "New Leaf City - Town", "url": "https://youtu.be/EXv5madDarI", "regions": {"id": 24, "town": "New Leaf City"}},
        {"id": 106, "name": "New Leaf City - Hunt", "url": "https://youtu.be/UB_Dn0LCYLE", "regions": {"id": 24, "town": "New Leaf City"}},
        {"id": 107, "name": "New Leaf City - Upbeat", "url": "https://youtu.be/d0kE_pLlE2U", "regions": {"id": 24, "town": "New Leaf City"}},
        {"id": 108, "name": "Phantom Forest (Original)", "url": "https://youtu.be/JDK9B4IWxdg", "regions": {"id": 25, "town": "Crimsonwood Keep"}},
        {"id": 109, "name": "Crimsonwood Keep", "url": "https://youtu.be/CZoYt7HHSik", "regions": {"id": 25, "town": "Crimsonwood Keep"}},
        {"id": 110, "name": "Bigfoot", "url": "https://youtu.be/X0pUdlLwIhA", "regions": {"id": 25, "town": "Crimsonwood Keep"}},
        {"id": 111, "name": "Crimsonwood Party Quest", "url": "https://youtu.be/xfq61ugRGBo", "regions": {"id": 25, "town": "Crimsonwood Keep"}},
        {"id": 112, "name": "Grandmaster's Gauntlet", "url": "https://youtu.be/rsASgHchliQ", "regions": {"id": 25, "town": "Crimsonwood Keep"}},
        {"id": 113, "name": "Crimsonwood Keep Interior", "url": "https://youtu.be/qbY2KUn3dmM", "regions": {"id": 25, "town": "Crimsonwood Keep"}},
        {"id": 114, "name": "Courtyard", "url": "https://youtu.be/h0_8MftVy90", "regions": {"id": 25, "town": "Crimsonwood Keep"}},
        {"id": 115, "name": "Haunted House", "url": "https://youtu.be/nbGQyrGizRQ", "regions": {"id": 26, "town": "Haunted House"}},
        {"id": 117, "name": "CBD Town", "url": "https://youtu.be/czDfxrSGea4", "regions": {"id": 27, "town": "Singapore"}},
        {"id": 118, "name": "CBD Field", "url": "https://youtu.be/MvheqAmubR8", "regions": {"id": 27, "town": "Singapore"}},
        {"id": 119, "name": "Boat Quay Town", "url": "https://youtu.be/GSDD0c_7FV0", "regions": {"id": 27, "town": "Singapore"}},
        {"id": 120, "name": "Boat Quay Field", "url": "https://youtu.be/DLdRypTOm0o", "regions": {"id": 27, "town": "Singapore"}},
        {"id": 121, "name": "Ghost Ship", "url": "https://youtu.be/cOatjxHHAEw", "regions": {"id": 27, "town": "Singapore"}},
        {"id": 122, "name": "Ulu Field", "url": "https://youtu.be/JIriGe2tdeA", "regions": {"id": 27, "town": "Singapore"}},
        {"id": 123, "name": "Kuala Lumpur", "url": "https://youtu.be/aJNseQp1Tb4", "regions": {"id": 28, "town": "Malaysia"}},
        {"id": 124, "name": "Highland", "url": "https://youtu.be/gNafzBfyoTo", "regions": {"id": 28, "town": "Malaysia"}},
        {"id": 125, "name": "Feeling", "url": "https://youtu.be/SdcsTuVLJk0", "regions": {"id": 29, "town": "Zipangu"}},
        {"id": 126, "name": "Bizarre Forest", "url": "https://youtu.be/9kmYUElcL_w", "regions": {"id": 29, "town": "Zipangu"}},
        {"id": 127, "name": "Castle Trap", "url": "https://youtu.be/c310tdhrwtk", "regions": {"id": 29, "town": "Zipangu"}},
        {"id": 128, "name": "Castle Outside", "url": "https://youtu.be/6yJ3_i6emNw", "regions": {"id": 29, "town": "Zipangu"}},
        {"id": 129, "name": "Castle Inside", "url": "https://youtu.be/8bvx6bZ8WnA", "regions": {"id": 29, "town": "Zipangu"}},
        {"id": 130, "name": "Castle Boss", "url": "https://youtu.be/_mSoAfONu6U", "regions": {"id": 29, "town": "Zipangu"}},
        {"id": 131, "name": "Yume", "url": "https://youtu.be/58QPkwCSd4Y", "regions": {"id": 30, "town": "Showa Town"}},
        {"id": 132, "name": "Bathroom", "url": "https://youtu.be/yRrCGa54Vbo", "regions": {"id": 30, "town": "Showa Town"}},
        {"id": 133, "name": "Battlefield", "url": "https://youtu.be/ZDS4Dd7ULvM", "regions": {"id": 30, "town": "Showa Town"}},
        {"id": 134, "name": "Golden Temple Town", "url": "https://youtu.be/Y_cihkgxF9A", "regions": {"id": 31, "town": "Golden Temple"}},
        {"id": 135, "name": "Golden Temple Field", "url": "https://youtu.be/NQPeBpjEYrs", "regions": {"id": 31, "town": "Golden Temple"}},
        {"id": 136, "name": "Golden Temple Dungeon", "url": "https://youtu.be/VoHtZ3sKsOY", "regions": {"id": 31, "town": "Golden Temple"}},
        {"id": 137, "name": "Elin Forest", "url": "https://youtu.be/8FShyABhIAs", "regions": {"id": 32, "town": "Ellin Forest"}},
        {"id": 138, "name": "Poison Forest", "url": "https://youtu.be/tc61Xjl4_X8", "regions": {"id": 32, "town": "Ellin Forest"}},
        {"id": 140, "name": "First Step Master", "url": "https://youtu.be/ePUZA7yRJVM", "regions": {"id": 33, "town": "Maple Island"}},
        {"id": 141, "name": "Queen's Garden", "url": "https://youtu.be/3r9s43TG9yA", "regions": {"id": 34, "town": "Ereve"}},
        {"id": 142, "name": "Raindrop Flower", "url": "https://youtu.be/DhUdOO9UNwY", "regions": {"id": 34, "town": "Ereve"}},
        {"id": 143, "name": "Drill Hall", "url": "https://youtu.be/uu55XbbIjRU", "regions": {"id": 34, "town": "Ereve"}},
        {"id": 144, "name": "Crystal Cave", "url": "https://youtu.be/Wr21LZPVPrw", "regions": {"id": 35, "town": "Rien"}},
        {"id": 145, "name": "Rien Village", "url": "https://youtu.be/YDfIfL_Fxec", "regions": {"id": 35, "town": "Rien"}},
        {"id": 146, "name": "Snow Drop", "url": "https://youtu.be/531E1H-sdSo", "regions": {"id": 35, "town": "Rien"}},
        {"id": 147, "name": "Bamboo Gym", "url": "https://youtu.be/9HiJnsISD3s", "regions": {"id": 35, "town": "Rien"}},
        {"id": 148, "name": "Amoria", "url": "https://youtu.be/hCdooZxzISo", "regions": {"id": 36, "town": "Amoria"}},
        {"id": 149, "name": "Cathedral", "url": "https://youtu.be/uqBUXZdBvVU", "regions": {"id": 36, "town": "Amoria"}},
        {"id": 150, "name": "Chapel", "url": "https://youtu.be/NJ6UMbOgQjU", "regions": {"id": 36, "town": "Amoria"}},
        {"id": 151, "name": "Amorian Challenge", "url": "https://youtu.be/fetvn2jzc9Q", "regions": {"id": 36, "town": "Amoria"}}
    ]
    
    return songs_data

def download_songs():
    """Download all songs as MP3 files"""
    songs = extract_song_data()
    
    # Create directories
    os.makedirs("bgm_files", exist_ok=True)
    
    failed_downloads = []
    
    print("Starting download of MapleStory BGM files...")
    print("Note: This requires FFmpeg to be installed for audio conversion.")
    print("You installed ffmpeg-python but still need the actual FFmpeg binary.")
    print("\nTo install FFmpeg on Windows:")
    print("1. Go to: https://ffmpeg.org/download.html")
    print("2. Download 'ffmpeg-release-full.7z' for Windows")
    print("3. Extract and add ffmpeg.exe to your system PATH")
    print("4. Or use: choco install ffmpeg (if you have Chocolatey)")
    print("\nContinuing without MP3 conversion - files will be saved as webm...\n")
    
    for i, song in enumerate(songs):
        print(f"Downloading {i+1}/{len(songs)}: {song['name']}")
        
        # Clean filename for this song
        clean_name = f"{song['name']} - {song['regions']['town']}"
        
        # Check if FFmpeg is available
        import subprocess
        try:
            subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
            ffmpeg_available = True
        except (subprocess.CalledProcessError, FileNotFoundError):
            ffmpeg_available = False
        
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
                'quiet': False,
                'no_warnings': False,
            }
        else:
            # Download without conversion - will save as webm
            ydl_opts = {
                'format': 'bestaudio[ext=webm]/bestaudio[ext=m4a]/bestaudio/best',
                'outtmpl': f'bgm_files/{clean_name}.%(ext)s',
                'quiet': False,
                'no_warnings': False,
            }
        
        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([song['url']])
                print(f"✓ Downloaded: {song['name']}")
                
        except Exception as e:
            error_msg = str(e)
            if "ffprobe and ffmpeg not found" in error_msg:
                print(f"✗ Failed to download {song['name']}: FFmpeg not found")
                print("  Please install FFmpeg to convert audio files")
                print("  Install with: pip install ffmpeg-python")
                print("  Or download from: https://ffmpeg.org/download.html")
                # Only show this message once
                if len(failed_downloads) == 0:
                    print("\nStopping downloads due to missing FFmpeg.")
                    print("Please install FFmpeg and try again.\n")
                    break
            else:
                print(f"✗ Failed to download {song['name']}: {error_msg}")
            failed_downloads.append(song)
        
        # Small delay to be respectful
        time.sleep(1)
    
    # Save metadata
    with open('songs_metadata.json', 'w', encoding='utf-8') as f:
        json.dump(songs, f, ensure_ascii=False, indent=2)
    
    print(f"\nDownload complete!")
    print(f"Successfully downloaded: {len(songs) - len(failed_downloads)}")
    print(f"Failed downloads: {len(failed_downloads)}")
    
    if failed_downloads:
        print("\nFailed songs:")
        for song in failed_downloads:
            print(f"  - {song['name']}")

if __name__ == "__main__":
    download_songs()
