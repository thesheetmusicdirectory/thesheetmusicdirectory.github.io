"""
Script to scrape guitar tabs from Ultimate Guitar for all 50 new songs.
Uses Selenium to handle JavaScript-rendered content.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import re
import os

# Song metadata with Ultimate Guitar URLs
songs = [
    {"filename": "wonderwall.html", "ug_link": "https://tabs.ultimate-guitar.com/tab/oasis/wonderwall-chords-27596"},
    {"filename": "hotel_california.html", "ug_link": "https://tabs.ultimate-guitar.com/tab/eagles/hotel-california-chords-46190"},
    {"filename": "stairway_to_heaven.html", "ug_link": "https://tabs.ultimate-guitar.com/tab/led-zeppelin/stairway-to-heaven-tabs-9488"},
    {"filename": "sweet_child_o__mine.html", "ug_link": "https://tabs.ultimate-guitar.com/tab/guns-n-roses/sweet-child-o-mine-tabs-9030"},
    {"filename": "imagine.html", "ug_link": "https://tabs.ultimate-guitar.com/tab/john-lennon/imagine-chords-9306"},
    {"filename": "hallelujah.html", "ug_link": "https://tabs.ultimate-guitar.com/tab/jeff-buckley/hallelujah-chords-198052"},
    {"filename": "wish_you_were_here.html", "ug_link": "https://tabs.ultimate-guitar.com/tab/pink-floyd/wish-you-were-here-chords-44555"},
    {"filename": "let_it_be.html", "ug_link": "https://tabs.ultimate-guitar.com/tab/the-beatles/let-it-be-chords-17427"},
    {"filename": "yesterday.html", "ug_link": "https://tabs.ultimate-guitar.com/tab/the-beatles/yesterday-chords-17450"},
    {"filename": "creep.html", "ug_link": "https://tabs.ultimate-guitar.com/tab/radiohead/creep-chords-4169"},
    # Add more songs as needed...
]

base_dir = r"c:\Users\matti\OneDrive\Documents\Code\thesheetmusicdirectory.github.io"

def scrape_tab_content(driver, url):
    """Scrape tab content from Ultimate Guitar URL"""
    try:
        driver.get(url)
        time.sleep(3)  # Wait for page to load
        
        # Try to accept cookies if present
        try:
            accept_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept') or contains(text(), 'I Accept')]"))
            )
            accept_button.click()
            time.sleep(2)
        except:
            pass  # No cookie banner or already accepted
        
        # Extract tab content using JavaScript
        script = """
        (() => {
            const content = document.body.innerText;
            const startMarker = '[Intro]';
            const endMarker = 'More Versions';
            const startIndex = content.indexOf(startMarker);
            if (startIndex === -1) return 'Start marker [Intro] not found';
            const tabStartIndex = startIndex;
            const endIndex = content.indexOf(endMarker, tabStartIndex);
            if (endIndex === -1) return 'End marker not found';
            return content.substring(tabStartIndex, endIndex).trim();
        })()
        """
        
        tab_content = driver.execute_script(script)
        
        if "not found" in tab_content.lower():
            print(f"⚠️  Could not extract tab content from {url}")
            return None
        
        return tab_content
        
    except Exception as e:
        print(f"❌ Error scraping {url}: {e}")
        return None

def update_html_file(filepath, tab_content):
    """Update HTML file with scraped tab content"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the tab content within <pre id="tabContent">
        pattern = r'(<pre id="tabContent">)(.*?)(</pre>)'
        
        def replace_content(match):
            return match.group(1) + '\n' + tab_content + '\n' + match.group(3)
        
        updated_content = re.sub(pattern, replace_content, content, flags=re.DOTALL)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"✅ Updated: {filepath}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating {filepath}: {e}")
        return False

def main():
    # Set up Chrome driver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in background
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    
    driver = webdriver.Chrome(options=options)
    
    try:
        for song in songs:
            print(f"\n🎵 Processing: {song['filename']}")
            
            # Scrape tab content
            tab_content = scrape_tab_content(driver, song['ug_link'])
            
            if tab_content:
                # Update HTML file
                filepath = os.path.join(base_dir, song['filename'])
                update_html_file(filepath, tab_content)
            else:
                print(f"⚠️  Skipping {song['filename']} - no content scraped")
            
            time.sleep(2)  # Be respectful to the server
        
        print("\n✅ Scraping complete!")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
