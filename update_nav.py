import os
import re

# List of all song files
song_files = [
    "bohemian_rhapsody.html",
    "back_in_black.html",
    "back_in_black_updated.html",
    "Dirty Deeds Done Dirt Cheap.html",
    "down_under.html",
    "free_bird.html",
    "hey_jude.html",
    "highway_star.html",
    "highway_to_hell_acdc.html",
    "house_of_the_rising_sun.html",
    "i_want_to_hold_your_hand.html",
    "johnny_b_goode.html",
    "sltsnirvana.html",
    "thunderstruck.html",
    "twist_and_shout.html"
]

base_dir = r"c:\Users\matti\OneDrive\Documents\Code\thesheetmusicdirectory.github.io"

for filename in song_files:
    filepath = os.path.join(base_dir, filename)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the Home link to add the arrow
        content = content.replace(
            '<a href="index.html" class="nav-link">Home</a>',
            '<a href="index.html" class="nav-link">← Home</a>'
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Updated: {filename}")
    except Exception as e:
        print(f"❌ Error updating {filename}: {e}")

print(f"\n✅ Updated navigation in {len(song_files)} song pages!")
