import requests
from bs4 import BeautifulSoup
import re
import os

# Song files and their URLs
songs = [
    {"filename": "bohemian_rhapsody.html", "url": "https://thesheetmusicdirectory.github.io/bohemian_rhapsody.html"},
    {"filename": "back_in_black.html", "url": "https://thesheetmusicdirectory.github.io/back_in_black.html"},
    {"filename": "back_in_black_updated.html", "url": "https://thesheetmusicdirectory.github.io/back_in_black_updated.html"},
    {"filename": "Dirty Deeds Done Dirt Cheap.html", "url": "https://thesheetmusicdirectory.github.io/Dirty%20Deeds%20Done%20Dirt%20Cheap.html"},
    {"filename": "down_under.html", "url": "https://thesheetmusicdirectory.github.io/down_under.html"},
    {"filename": "free_bird.html", "url": "https://thesheetmusicdirectory.github.io/free_bird.html"},
    {"filename": "hey_jude.html", "url": "https://thesheetmusicdirectory.github.io/hey_jude.html"},
    {"filename": "highway_star.html", "url": "https://thesheetmusicdirectory.github.io/highway_star.html"},
    {"filename": "highway_to_hell_acdc.html", "url": "https://thesheetmusicdirectory.github.io/highway_to_hell_acdc.html"},
    {"filename": "house_of_the_rising_sun.html", "url": "https://thesheetmusicdirectory.github.io/house_of_the_rising_sun.html"},
    {"filename": "i_want_to_hold_your_hand.html", "url": "https://thesheetmusicdirectory.github.io/i_want_to_hold_your_hand.html"},
    {"filename": "johnny_b_goode.html", "url": "https://thesheetmusicdirectory.github.io/johnny_b_goode.html"},
    {"filename": "sltsnirvana.html", "url": "https://thesheetmusicdirectory.github.io/sltsnirvana.html"},
    {"filename": "thunderstruck.html", "url": "https://thesheetmusicdirectory.github.io/thunderstruck.html"},
    {"filename": "twist_and_shout.html", "url": "https://thesheetmusicdirectory.github.io/twist_and_shout.html"}
]

base_dir = r"c:\Users\matti\OneDrive\Documents\Code\thesheetmusicdirectory.github.io"
scraped_tabs = {}

print("🌐 Scraping tab content from live website...\n")

for song in songs:
    try:
        # Fetch the live page
        response = requests.get(song["url"], timeout=10)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the <pre> tag with tab content
        pre_tag = soup.find('pre', id='tabContent')
        if not pre_tag:
            pre_tag = soup.find('pre')
        
        if pre_tag:
            tab_content = pre_tag.get_text()
            scraped_tabs[song["filename"]] = tab_content
            print(f"✅ Scraped: {song['filename']} ({len(tab_content)} chars)")
        else:
            print(f"⚠️  No tab content found: {song['filename']}")
            scraped_tabs[song["filename"]] = "Tab content not found"
            
    except Exception as e:
        print(f"❌ Error scraping {song['filename']}: {e}")
        scraped_tabs[song["filename"]] = "Tab content not found"

print(f"\n📝 Updating local files with scraped content...\n")

# Now update local files with scraped content
for song in songs:
    filepath = os.path.join(base_dir, song["filename"])
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Get the scraped tab content
        tab_content = scraped_tabs.get(song["filename"], "Tab content not found")
        
        # Escape special regex characters in the tab content
        escaped_content = re.escape(tab_content)
        
        # Replace the tab content in the <pre> tag
        pattern = r'(<pre id="tabContent">)(.*?)(</pre>)'
        replacement = r'\1' + tab_content + r'\3'
        
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Updated: {song['filename']}")
        
    except Exception as e:
        print(f"❌ Error updating {song['filename']}: {e}")

print(f"\n✅ Scraping and update complete!")
