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
        
        # Update the .page-header CSS to match content.html (more padding, no border)
        old_header_css = r"""        .page-header {
            background: #fff;
            border-bottom: 1px solid var(--border-color);
            padding: 1rem 2rem
        }"""
        
        new_header_css = """        .page-header {
            padding: 4rem 2rem;
            background: #fff;
            text-align: center
        }"""
        
        content = content.replace(old_header_css, new_header_css)
        
        # Update the .header-nav CSS to match content.html
        old_nav_css = r"""        .header-nav {
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-bottom: 0.5rem
        }"""
        
        new_nav_css = """        .header-nav {
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-bottom: 2rem
        }"""
        
        content = content.replace(old_nav_css, new_nav_css)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Updated: {filename}")
    except Exception as e:
        print(f"❌ Error updating {filename}: {e}")

print(f"\n✅ Updated header styling in {len(song_files)} song pages!")
