# Song Page Batch Updater
# This script updates all song pages to use the Material Design template

import os
import re

# Song metadata - extracted from existing files
songs = [
    {
        "filename": "bohemian_rhapsody.html",
        "song_id": "bohemianrhapsody",
        "title": "Bohemian Rhapsody",
        "artist": "Queen",
        "icon": "🎸",
        "difficulty": "Advanced",
        "difficulty_icon": "trending_up",
        "instrument": "Guitar",
        "instrument_icon": "music_note",
        "genre": "Progressive Rock",
        "genre_icon": "album",
        "tab_type": "Guitar Tabs",
        "default_bpm": "72",
        "wiki_link": "https://en.wikipedia.org/wiki/Bohemian_Rhapsody",
        "ug_link": "https://tabs.ultimate-guitar.com/tab/queen/bohemian-rhapsody-tabs-45188",
        "youtube_link": "https://www.youtube.com/results?search_query=bohemian+rhapsody+guitar+tutorial"
    },
    {
        "filename": "back_in_black.html",
        "song_id": "backinblack",
        "title": "Back in Black",
        "artist": "AC/DC",
        "icon": "⚡",
        "difficulty": "Intermediate",
        "difficulty_icon": "show_chart",
        "instrument": "Guitar",
        "instrument_icon": "music_note",
        "genre": "Hard Rock",
        "genre_icon": "album",
        "tab_type": "Guitar Tabs",
        "default_bpm": "94",
        "wiki_link": "https://en.wikipedia.org/wiki/Back_in_Black",
        "ug_link": "https://tabs.ultimate-guitar.com/tab/ac-dc/back-in-black-tabs-26534",
        "youtube_link": "https://www.youtube.com/results?search_query=back+in+black+guitar+tutorial"
    },
    {
        "filename": "back_in_black_updated.html",
        "song_id": "backinblackupdated",
        "title": "Back in Black",
        "artist": "AC/DC",
        "icon": "⚡",
        "difficulty": "Intermediate",
        "difficulty_icon": "show_chart",
        "instrument": "Guitar",
        "instrument_icon": "music_note",
        "genre": "Hard Rock",
        "genre_icon": "album",
        "tab_type": "Guitar Tabs (Updated)",
        "default_bpm": "94",
        "wiki_link": "https://en.wikipedia.org/wiki/Back_in_Black",
        "ug_link": "https://tabs.ultimate-guitar.com/tab/ac-dc/back-in-black-tabs-26534",
        "youtube_link": "https://www.youtube.com/results?search_query=back+in+black+guitar+tutorial"
    },
    {
        "filename": "Dirty Deeds Done Dirt Cheap.html",
        "song_id": "dirtydeedsdone",
        "title": "Dirty Deeds Done Dirt Cheap",
        "artist": "AC/DC",
        "icon": "⚡",
        "difficulty": "Beginner",
        "difficulty_icon": "trending_flat",
        "instrument": "Guitar",
        "instrument_icon": "music_note",
        "genre": "Hard Rock",
        "genre_icon": "album",
        "tab_type": "Guitar Tabs",
        "default_bpm": "120",
        "wiki_link": "https://en.wikipedia.org/wiki/Dirty_Deeds_Done_Dirt_Cheap",
        "ug_link": "https://tabs.ultimate-guitar.com/tab/ac-dc/dirty-deeds-done-dirt-cheap-tabs-26535",
        "youtube_link": "https://www.youtube.com/results?search_query=dirty+deeds+done+dirt+cheap+guitar+tutorial"
    },
    {
        "filename": "down_under.html",
        "song_id": "downunder",
        "title": "Down Under",
        "artist": "Men at Work",
        "icon": "🎺",
        "difficulty": "Intermediate",
        "difficulty_icon": "show_chart",
        "instrument": "Guitar",
        "instrument_icon": "music_note",
        "genre": "New Wave",
        "genre_icon": "album",
        "tab_type": "Guitar Tabs",
        "default_bpm": "104",
        "wiki_link": "https://en.wikipedia.org/wiki/Down_Under_(song)",
        "ug_link": "https://tabs.ultimate-guitar.com/tab/men-at-work/down-under-tabs-26536",
        "youtube_link": "https://www.youtube.com/results?search_query=down+under+guitar+tutorial"
    },
    {
        "filename": "free_bird.html",
        "song_id": "freebird",
        "title": "Free Bird",
        "artist": "Lynyrd Skynyrd",
        "icon": "🦅",
        "difficulty": "Advanced",
        "difficulty_icon": "trending_up",
        "instrument": "Guitar",
        "instrument_icon": "music_note",
        "genre": "Southern Rock",
        "genre_icon": "album",
        "tab_type": "Guitar Tabs",
        "default_bpm": "60",
        "wiki_link": "https://en.wikipedia.org/wiki/Free_Bird",
        "ug_link": "https://tabs.ultimate-guitar.com/tab/lynyrd-skynyrd/free-bird-tabs-26537",
        "youtube_link": "https://www.youtube.com/results?search_query=free+bird+guitar+tutorial"
    },
    {
        "filename": "hey_jude.html",
        "song_id": "heyjude",
        "title": "Hey Jude",
        "artist": "The Beatles",
        "icon": "🎹",
        "difficulty": "Beginner",
        "difficulty_icon": "trending_flat",
        "instrument": "Piano",
        "instrument_icon": "piano",
        "genre": "Rock",
        "genre_icon": "album",
        "tab_type": "Piano Score",
        "default_bpm": "73",
        "wiki_link": "https://en.wikipedia.org/wiki/Hey_Jude",
        "ug_link": "https://tabs.ultimate-guitar.com/tab/the-beatles/hey-jude-tabs-26538",
        "youtube_link": "https://www.youtube.com/results?search_query=hey+jude+piano+tutorial"
    },
    {
        "filename": "highway_star.html",
        "song_id": "highwaystar",
        "title": "Highway Star",
        "artist": "Deep Purple",
        "icon": "🎸",
        "difficulty": "Advanced",
        "difficulty_icon": "trending_up",
        "instrument": "Guitar",
        "instrument_icon": "music_note",
        "genre": "Hard Rock",
        "genre_icon": "album",
        "tab_type": "Guitar Tabs",
        "default_bpm": "180",
        "wiki_link": "https://en.wikipedia.org/wiki/Highway_Star_(song)",
        "ug_link": "https://tabs.ultimate-guitar.com/tab/deep-purple/highway-star-tabs-26539",
        "youtube_link": "https://www.youtube.com/results?search_query=highway+star+guitar+tutorial"
    },
    {
        "filename": "highway_to_hell_acdc.html",
        "song_id": "highwaytohell",
        "title": "Highway to Hell",
        "artist": "AC/DC",
        "icon": "⚡",
        "difficulty": "Intermediate",
        "difficulty_icon": "show_chart",
        "instrument": "Guitar",
        "instrument_icon": "music_note",
        "genre": "Hard Rock",
        "genre_icon": "album",
        "tab_type": "Guitar Tabs",
        "default_bpm": "116",
        "wiki_link": "https://en.wikipedia.org/wiki/Highway_to_Hell_(song)",
        "ug_link": "https://tabs.ultimate-guitar.com/tab/ac-dc/highway-to-hell-tabs-26540",
        "youtube_link": "https://www.youtube.com/results?search_query=highway+to+hell+guitar+tutorial"
    },
    {
        "filename": "house_of_the_rising_sun.html",
        "song_id": "houseoftherisingsun",
        "title": "House of the Rising Sun",
        "artist": "The Animals",
        "icon": "🌅",
        "difficulty": "Intermediate",
        "difficulty_icon": "show_chart",
        "instrument": "Guitar",
        "instrument_icon": "music_note",
        "genre": "Folk Rock",
        "genre_icon": "album",
        "tab_type": "Guitar Tabs",
        "default_bpm": "96",
        "wiki_link": "https://en.wikipedia.org/wiki/The_House_of_the_Rising_Sun",
        "ug_link": "https://tabs.ultimate-guitar.com/tab/the-animals/house-of-the-rising-sun-tabs-26541",
        "youtube_link": "https://www.youtube.com/results?search_query=house+of+the+rising+sun+guitar+tutorial"
    },
    {
        "filename": "i_want_to_hold_your_hand.html",
        "song_id": "iwanttoholdyourhand",
        "title": "I Want to Hold Your Hand",
        "artist": "The Beatles",
        "icon": "🎸",
        "difficulty": "Beginner",
        "difficulty_icon": "trending_flat",
        "instrument": "Guitar",
        "instrument_icon": "music_note",
        "genre": "Pop Rock",
        "genre_icon": "album",
        "tab_type": "Guitar Tabs",
        "default_bpm": "130",
        "wiki_link": "https://en.wikipedia.org/wiki/I_Want_to_Hold_Your_Hand",
        "ug_link": "https://tabs.ultimate-guitar.com/tab/the-beatles/i-want-to-hold-your-hand-tabs-26542",
        "youtube_link": "https://www.youtube.com/results?search_query=i+want+to+hold+your+hand+guitar+tutorial"
    },
    {
        "filename": "johnny_b_goode.html",
        "song_id": "johnnybgoode",
        "title": "Johnny B. Goode",
        "artist": "Chuck Berry",
        "icon": "🎸",
        "difficulty": "Advanced",
        "difficulty_icon": "trending_up",
        "instrument": "Guitar",
        "instrument_icon": "music_note",
        "genre": "Rock and Roll",
        "genre_icon": "album",
        "tab_type": "Guitar Tabs",
        "default_bpm": "168",
        "wiki_link": "https://en.wikipedia.org/wiki/Johnny_B._Goode",
        "ug_link": "https://tabs.ultimate-guitar.com/tab/chuck-berry/johnny-b-goode-tabs-26543",
        "youtube_link": "https://www.youtube.com/results?search_query=johnny+b+goode+guitar+tutorial"
    },
    {
        "filename": "sltsnirvana.html",
        "song_id": "smellsliketeenspirit",
        "title": "Smells Like Teen Spirit",
        "artist": "Nirvana",
        "icon": "🎸",
        "difficulty": "Intermediate",
        "difficulty_icon": "show_chart",
        "instrument": "Guitar",
        "instrument_icon": "music_note",
        "genre": "Grunge",
        "genre_icon": "album",
        "tab_type": "Guitar Tabs",
        "default_bpm": "116",
        "wiki_link": "https://en.wikipedia.org/wiki/Smells_Like_Teen_Spirit",
        "ug_link": "https://tabs.ultimate-guitar.com/tab/nirvana/smells-like-teen-spirit-tabs-26544",
        "youtube_link": "https://www.youtube.com/results?search_query=smells+like+teen+spirit+guitar+tutorial"
    },
    {
        "filename": "thunderstruck.html",
        "song_id": "thunderstruck",
        "title": "Thunderstruck",
        "artist": "AC/DC",
        "icon": "⚡",
        "difficulty": "Advanced",
        "difficulty_icon": "trending_up",
        "instrument": "Guitar",
        "instrument_icon": "music_note",
        "genre": "Hard Rock",
        "genre_icon": "album",
        "tab_type": "Guitar Tabs",
        "default_bpm": "133",
        "wiki_link": "https://en.wikipedia.org/wiki/Thunderstruck_(song)",
        "ug_link": "https://tabs.ultimate-guitar.com/tab/ac-dc/thunderstruck-tabs-26545",
        "youtube_link": "https://www.youtube.com/results?search_query=thunderstruck+guitar+tutorial"
    },
    {
        "filename": "twist_and_shout.html",
        "song_id": "twistandshout",
        "title": "Twist and Shout",
        "artist": "The Beatles",
        "icon": "🎸",
        "difficulty": "Beginner",
        "difficulty_icon": "trending_flat",
        "instrument": "Guitar",
        "instrument_icon": "music_note",
        "genre": "Rock and Roll",
        "genre_icon": "album",
        "tab_type": "Guitar Tabs",
        "default_bpm": "126",
        "wiki_link": "https://en.wikipedia.org/wiki/Twist_and_Shout",
        "ug_link": "https://tabs.ultimate-guitar.com/tab/the-beatles/twist-and-shout-tabs-26546",
        "youtube_link": "https://www.youtube.com/results?search_query=twist+and+shout+guitar+tutorial"
    }
]

def extract_tab_content(filepath):
    """Extract the tab content from existing song file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Find content between <pre> tags (case-insensitive, allow attributes)
            match = re.search(r'<pre[^>]*>(.*?)</pre>', content, re.DOTALL | re.IGNORECASE)
            if match:
                return match.group(1).strip()
    except:
        pass
    return "Tab content not found"

def create_song_page(template_path, song_data, output_path, tab_content):
    """Create a song page from template"""
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Replace all placeholders
    replacements = {
        '{{SONG_TITLE}}': song_data['title'],
        '{{ARTIST_NAME}}': song_data['artist'],
        '{{ICON_EMOJI}}': song_data['icon'],
        '{{DIFFICULTY}}': song_data['difficulty'],
        '{{DIFFICULTY_ICON}}': song_data['difficulty_icon'],
        '{{INSTRUMENT}}': song_data['instrument'],
        '{{INSTRUMENT_ICON}}': song_data['instrument_icon'],
        '{{GENRE}}': song_data['genre'],
        '{{GENRE_ICON}}': song_data['genre_icon'],
        '{{TAB_TYPE}}': song_data['tab_type'],
        '{{DEFAULT_BPM}}': song_data['default_bpm'],
        '{{SONG_ID}}': song_data['song_id'],
        '{{WIKI_LINK}}': song_data['wiki_link'],
        '{{UG_LINK}}': song_data['ug_link'],
        '{{YOUTUBE_LINK}}': song_data['youtube_link'],
        '{{TAB_CONTENT}}': tab_content
    }
    
    result = template
    for placeholder, value in replacements.items():
        result = result.replace(placeholder, value)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result)
    
    print(f"✅ Created: {output_path}")

# Main execution
if __name__ == "__main__":
    base_dir = r"c:\Users\matti\OneDrive\Documents\Code\thesheetmusicdirectory.github.io"
    template_path = os.path.join(base_dir, "song_template.html")
    
    for song in songs:
        input_path = os.path.join(base_dir, song['filename'])
        output_path = input_path  # Overwrite existing file
        
        # Extract tab content from existing file
        tab_content = extract_tab_content(input_path)
        
        # Create new page from template
        create_song_page(template_path, song, output_path, tab_content)
    
    print(f"\n✅ Updated {len(songs)} song pages!")
