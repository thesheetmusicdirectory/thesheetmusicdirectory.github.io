import os
import re

# List of 50 songs with metadata
new_songs = [
    {"title": "Wonderwall", "artist": "Oasis", "genre": "Britpop", "difficulty": "Beginner", "icon": "🎸", "difficulty_icon": "trending_flat", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "88", "wiki_link": "https://en.wikipedia.org/wiki/Wonderwall_(song)", "ug_link": "https://tabs.ultimate-guitar.com/tab/oasis/wonderwall-chords-27596", "youtube_link": "https://www.youtube.com/results?search_query=wonderwall+guitar+tutorial"},
    {"title": "Hotel California", "artist": "Eagles", "genre": "Rock", "difficulty": "Intermediate", "icon": "🏨", "difficulty_icon": "show_chart", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "75", "wiki_link": "https://en.wikipedia.org/wiki/Hotel_California", "ug_link": "https://tabs.ultimate-guitar.com/tab/eagles/hotel-california-chords-46190", "youtube_link": "https://www.youtube.com/results?search_query=hotel+california+guitar+tutorial"},
    {"title": "Stairway to Heaven", "artist": "Led Zeppelin", "genre": "Rock", "difficulty": "Advanced", "icon": "🪜", "difficulty_icon": "trending_up", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Tabs", "default_bpm": "82", "wiki_link": "https://en.wikipedia.org/wiki/Stairway_to_Heaven", "ug_link": "https://tabs.ultimate-guitar.com/tab/led-zeppelin/stairway-to-heaven-tabs-9488", "youtube_link": "https://www.youtube.com/results?search_query=stairway+to+heaven+guitar+tutorial"},
    {"title": "Sweet Child O' Mine", "artist": "Guns N' Roses", "genre": "Hard Rock", "difficulty": "Advanced", "icon": "🌹", "difficulty_icon": "trending_up", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Tabs", "default_bpm": "125", "wiki_link": "https://en.wikipedia.org/wiki/Sweet_Child_o%27_Mine", "ug_link": "https://tabs.ultimate-guitar.com/tab/guns-n-roses/sweet-child-o-mine-tabs-9030", "youtube_link": "https://www.youtube.com/results?search_query=sweet+child+o+mine+guitar+tutorial"},
    {"title": "Imagine", "artist": "John Lennon", "genre": "Pop", "difficulty": "Beginner", "icon": "🎹", "difficulty_icon": "trending_flat", "instrument": "Piano", "instrument_icon": "piano", "genre_icon": "album", "tab_type": "Piano Chords", "default_bpm": "76", "wiki_link": "https://en.wikipedia.org/wiki/Imagine_(John_Lennon_song)", "ug_link": "https://tabs.ultimate-guitar.com/tab/john-lennon/imagine-chords-9306", "youtube_link": "https://www.youtube.com/results?search_query=imagine+piano+tutorial"},
    {"title": "Hallelujah", "artist": "Jeff Buckley", "genre": "Alternative", "difficulty": "Intermediate", "icon": "🙏", "difficulty_icon": "show_chart", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "56", "wiki_link": "https://en.wikipedia.org/wiki/Hallelujah_(Leonard_Cohen_song)", "ug_link": "https://tabs.ultimate-guitar.com/tab/jeff-buckley/hallelujah-chords-198052", "youtube_link": "https://www.youtube.com/results?search_query=hallelujah+jeff+buckley+guitar+tutorial"},
    {"title": "Wish You Were Here", "artist": "Pink Floyd", "genre": "Rock", "difficulty": "Intermediate", "icon": "💎", "difficulty_icon": "show_chart", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "60", "wiki_link": "https://en.wikipedia.org/wiki/Wish_You_Were_Here_(Pink_Floyd_song)", "ug_link": "https://tabs.ultimate-guitar.com/tab/pink-floyd/wish-you-were-here-chords-44555", "youtube_link": "https://www.youtube.com/results?search_query=wish+you+were+here+guitar+tutorial"},
    {"title": "Let It Be", "artist": "The Beatles", "genre": "Pop Rock", "difficulty": "Beginner", "icon": "🐞", "difficulty_icon": "trending_flat", "instrument": "Piano", "instrument_icon": "piano", "genre_icon": "album", "tab_type": "Piano Chords", "default_bpm": "143", "wiki_link": "https://en.wikipedia.org/wiki/Let_It_Be_(Beatles_song)", "ug_link": "https://tabs.ultimate-guitar.com/tab/the-beatles/let-it-be-chords-17427", "youtube_link": "https://www.youtube.com/results?search_query=let+it+be+piano+tutorial"},
    {"title": "Yesterday", "artist": "The Beatles", "genre": "Pop", "difficulty": "Intermediate", "icon": "📅", "difficulty_icon": "show_chart", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "97", "wiki_link": "https://en.wikipedia.org/wiki/Yesterday", "ug_link": "https://tabs.ultimate-guitar.com/tab/the-beatles/yesterday-chords-17450", "youtube_link": "https://www.youtube.com/results?search_query=yesterday+guitar+tutorial"},
    {"title": "Creep", "artist": "Radiohead", "genre": "Alternative", "difficulty": "Beginner", "icon": "📻", "difficulty_icon": "trending_flat", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "92", "wiki_link": "https://en.wikipedia.org/wiki/Creep_(Radiohead_song)", "ug_link": "https://tabs.ultimate-guitar.com/tab/radiohead/creep-chords-4169", "youtube_link": "https://www.youtube.com/results?search_query=creep+radiohead+guitar+tutorial"},
    {"title": "Californication", "artist": "Red Hot Chili Peppers", "genre": "Alternative", "difficulty": "Intermediate", "icon": "🌶️", "difficulty_icon": "show_chart", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Tabs", "default_bpm": "96", "wiki_link": "https://en.wikipedia.org/wiki/Californication_(song)", "ug_link": "https://tabs.ultimate-guitar.com/tab/red-hot-chili-peppers/californication-tabs-57849", "youtube_link": "https://www.youtube.com/results?search_query=californication+guitar+tutorial"},
    {"title": "Under the Bridge", "artist": "Red Hot Chili Peppers", "genre": "Alternative", "difficulty": "Intermediate", "icon": "🌉", "difficulty_icon": "show_chart", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "84", "wiki_link": "https://en.wikipedia.org/wiki/Under_the_Bridge", "ug_link": "https://tabs.ultimate-guitar.com/tab/red-hot-chili-peppers/under-the-bridge-chords-7140", "youtube_link": "https://www.youtube.com/results?search_query=under+the+bridge+guitar+tutorial"},
    {"title": "Blackbird", "artist": "The Beatles", "genre": "Folk", "difficulty": "Intermediate", "icon": "🐦", "difficulty_icon": "show_chart", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Tabs", "default_bpm": "94", "wiki_link": "https://en.wikipedia.org/wiki/Blackbird_(Beatles_song)", "ug_link": "https://tabs.ultimate-guitar.com/tab/the-beatles/blackbird-tabs-57698", "youtube_link": "https://www.youtube.com/results?search_query=blackbird+guitar+tutorial"},
    {"title": "Good Riddance (Time of Your Life)", "artist": "Green Day", "genre": "Punk Rock", "difficulty": "Beginner", "icon": "🕰️", "difficulty_icon": "trending_flat", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "95", "wiki_link": "https://en.wikipedia.org/wiki/Good_Riddance_(Time_of_Your_Life)", "ug_link": "https://tabs.ultimate-guitar.com/tab/green-day/good-riddance-time-of-your-life-chords-12835", "youtube_link": "https://www.youtube.com/results?search_query=good+riddance+green+day+guitar+tutorial"},
    {"title": "Seven Nation Army", "artist": "The White Stripes", "genre": "Rock", "difficulty": "Beginner", "icon": "7️⃣", "difficulty_icon": "trending_flat", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Tabs", "default_bpm": "124", "wiki_link": "https://en.wikipedia.org/wiki/Seven_Nation_Army", "ug_link": "https://tabs.ultimate-guitar.com/tab/the-white-stripes/seven-nation-army-tabs-58836", "youtube_link": "https://www.youtube.com/results?search_query=seven+nation+army+guitar+tutorial"},
    {"title": "Zombie", "artist": "The Cranberries", "genre": "Alternative", "difficulty": "Beginner", "icon": "🧟", "difficulty_icon": "trending_flat", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "84", "wiki_link": "https://en.wikipedia.org/wiki/Zombie_(The_Cranberries_song)", "ug_link": "https://tabs.ultimate-guitar.com/tab/the-cranberries/zombie-chords-844902", "youtube_link": "https://www.youtube.com/results?search_query=zombie+cranberries+guitar+tutorial"},
    {"title": "Knockin' on Heaven's Door", "artist": "Bob Dylan", "genre": "Folk", "difficulty": "Beginner", "icon": "🚪", "difficulty_icon": "trending_flat", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "140", "wiki_link": "https://en.wikipedia.org/wiki/Knockin%27_on_Heaven%27s_Door", "ug_link": "https://tabs.ultimate-guitar.com/tab/bob-dylan/knockin-on-heavens-door-chords-66559", "youtube_link": "https://www.youtube.com/results?search_query=knockin+on+heavens+door+guitar+tutorial"},
    {"title": "Sweet Home Alabama", "artist": "Lynyrd Skynyrd", "genre": "Southern Rock", "difficulty": "Intermediate", "icon": "🏠", "difficulty_icon": "show_chart", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Tabs", "default_bpm": "98", "wiki_link": "https://en.wikipedia.org/wiki/Sweet_Home_Alabama", "ug_link": "https://tabs.ultimate-guitar.com/tab/lynyrd-skynyrd/sweet-home-alabama-tabs-58978", "youtube_link": "https://www.youtube.com/results?search_query=sweet+home+alabama+guitar+tutorial"},
    {"title": "Nothing Else Matters", "artist": "Metallica", "genre": "Metal", "difficulty": "Intermediate", "icon": "🤘", "difficulty_icon": "show_chart", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Tabs", "default_bpm": "46", "wiki_link": "https://en.wikipedia.org/wiki/Nothing_Else_Matters", "ug_link": "https://tabs.ultimate-guitar.com/tab/metallica/nothing-else-matters-tabs-8519", "youtube_link": "https://www.youtube.com/results?search_query=nothing+else+matters+guitar+tutorial"},
    {"title": "Enter Sandman", "artist": "Metallica", "genre": "Metal", "difficulty": "Intermediate", "icon": "🛌", "difficulty_icon": "show_chart", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Tabs", "default_bpm": "123", "wiki_link": "https://en.wikipedia.org/wiki/Enter_Sandman", "ug_link": "https://tabs.ultimate-guitar.com/tab/metallica/enter-sandman-tabs-6825", "youtube_link": "https://www.youtube.com/results?search_query=enter+sandman+guitar+tutorial"},
    {"title": "Smells Like Teen Spirit", "artist": "Nirvana", "genre": "Grunge", "difficulty": "Intermediate", "icon": "👃", "difficulty_icon": "show_chart", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Tabs", "default_bpm": "117", "wiki_link": "https://en.wikipedia.org/wiki/Smells_Like_Teen_Spirit", "ug_link": "https://tabs.ultimate-guitar.com/tab/nirvana/smells-like-teen-spirit-tabs-202727", "youtube_link": "https://www.youtube.com/results?search_query=smells+like+teen+spirit+guitar+tutorial"},
    {"title": "Come As You Are", "artist": "Nirvana", "genre": "Grunge", "difficulty": "Beginner", "icon": "🔫", "difficulty_icon": "trending_flat", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Tabs", "default_bpm": "120", "wiki_link": "https://en.wikipedia.org/wiki/Come_as_You_Are_(Nirvana_song)", "ug_link": "https://tabs.ultimate-guitar.com/tab/nirvana/come-as-you-are-tabs-56968", "youtube_link": "https://www.youtube.com/results?search_query=come+as+you+are+guitar+tutorial"},
    {"title": "Boulevard of Broken Dreams", "artist": "Green Day", "genre": "Punk Rock", "difficulty": "Beginner", "icon": "🚶", "difficulty_icon": "trending_flat", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "83", "wiki_link": "https://en.wikipedia.org/wiki/Boulevard_of_Broken_Dreams_(Green_Day_song)", "ug_link": "https://tabs.ultimate-guitar.com/tab/green-day/boulevard-of-broken-dreams-chords-130466", "youtube_link": "https://www.youtube.com/results?search_query=boulevard+of+broken+dreams+guitar+tutorial"},
    {"title": "Basket Case", "artist": "Green Day", "genre": "Punk Rock", "difficulty": "Intermediate", "icon": "🧺", "difficulty_icon": "show_chart", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "175", "wiki_link": "https://en.wikipedia.org/wiki/Basket_Case_(song)", "ug_link": "https://tabs.ultimate-guitar.com/tab/green-day/basket-case-chords-1065", "youtube_link": "https://www.youtube.com/results?search_query=basket+case+guitar+tutorial"},
    {"title": "American Idiot", "artist": "Green Day", "genre": "Punk Rock", "difficulty": "Intermediate", "icon": "🇺🇸", "difficulty_icon": "show_chart", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Tabs", "default_bpm": "186", "wiki_link": "https://en.wikipedia.org/wiki/American_Idiot_(song)", "ug_link": "https://tabs.ultimate-guitar.com/tab/green-day/american-idiot-tabs-157975", "youtube_link": "https://www.youtube.com/results?search_query=american+idiot+guitar+tutorial"},
    {"title": "Mr. Brightside", "artist": "The Killers", "genre": "Alternative", "difficulty": "Intermediate", "icon": "🌟", "difficulty_icon": "show_chart", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Tabs", "default_bpm": "148", "wiki_link": "https://en.wikipedia.org/wiki/Mr._Brightside", "ug_link": "https://tabs.ultimate-guitar.com/tab/the-killers/mr-brightside-tabs-167822", "youtube_link": "https://www.youtube.com/results?search_query=mr+brightside+guitar+tutorial"},
    {"title": "Don't Stop Believin'", "artist": "Journey", "genre": "Rock", "difficulty": "Intermediate", "icon": "🚂", "difficulty_icon": "show_chart", "instrument": "Piano", "instrument_icon": "piano", "genre_icon": "album", "tab_type": "Piano Chords", "default_bpm": "119", "wiki_link": "https://en.wikipedia.org/wiki/Don%27t_Stop_Believin%27", "ug_link": "https://tabs.ultimate-guitar.com/tab/journey/dont-stop-believin-chords-210470", "youtube_link": "https://www.youtube.com/results?search_query=dont+stop+believin+piano+tutorial"},
    {"title": "Livin' on a Prayer", "artist": "Bon Jovi", "genre": "Rock", "difficulty": "Intermediate", "icon": "🙏", "difficulty_icon": "show_chart", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "123", "wiki_link": "https://en.wikipedia.org/wiki/Livin%27_on_a_Prayer", "ug_link": "https://tabs.ultimate-guitar.com/tab/bon-jovi/livin-on-a-prayer-chords-10563", "youtube_link": "https://www.youtube.com/results?search_query=livin+on+a+prayer+guitar+tutorial"},
    {"title": "Africa", "artist": "Toto", "genre": "Pop", "difficulty": "Intermediate", "icon": "🌍", "difficulty_icon": "show_chart", "instrument": "Piano", "instrument_icon": "piano", "genre_icon": "album", "tab_type": "Piano Chords", "default_bpm": "92", "wiki_link": "https://en.wikipedia.org/wiki/Africa_(Toto_song)", "ug_link": "https://tabs.ultimate-guitar.com/tab/toto/africa-chords-25372", "youtube_link": "https://www.youtube.com/results?search_query=africa+toto+piano+tutorial"},
    {"title": "Take Me Home, Country Roads", "artist": "John Denver", "genre": "Folk", "difficulty": "Beginner", "icon": "🛣️", "difficulty_icon": "trending_flat", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "82", "wiki_link": "https://en.wikipedia.org/wiki/Take_Me_Home,_Country_Roads", "ug_link": "https://tabs.ultimate-guitar.com/tab/john-denver/take-me-home-country-roads-chords-10508", "youtube_link": "https://www.youtube.com/results?search_query=country+roads+guitar+tutorial"},
    {"title": "Jolene", "artist": "Dolly Parton", "genre": "Country", "difficulty": "Beginner", "icon": "👩", "difficulty_icon": "trending_flat", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "110", "wiki_link": "https://en.wikipedia.org/wiki/Jolene_(song)", "ug_link": "https://tabs.ultimate-guitar.com/tab/dolly-parton/jolene-chords-183011", "youtube_link": "https://www.youtube.com/results?search_query=jolene+guitar+tutorial"},
    {"title": "Ring of Fire", "artist": "Johnny Cash", "genre": "Country", "difficulty": "Beginner", "icon": "🔥", "difficulty_icon": "trending_flat", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "104", "wiki_link": "https://en.wikipedia.org/wiki/Ring_of_Fire_(song)", "ug_link": "https://tabs.ultimate-guitar.com/tab/johnny-cash/ring-of-fire-chords-10515", "youtube_link": "https://www.youtube.com/results?search_query=ring+of+fire+guitar+tutorial"},
    {"title": "Hurt", "artist": "Johnny Cash", "genre": "Folk", "difficulty": "Beginner", "icon": "😢", "difficulty_icon": "trending_flat", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "92", "wiki_link": "https://en.wikipedia.org/wiki/Hurt_(Nine_Inch_Nails_song)#Johnny_Cash_version", "ug_link": "https://tabs.ultimate-guitar.com/tab/johnny-cash/hurt-chords-42777", "youtube_link": "https://www.youtube.com/results?search_query=hurt+johnny+cash+guitar+tutorial"},
    {"title": "Sound of Silence", "artist": "Simon & Garfunkel", "genre": "Folk", "difficulty": "Intermediate", "icon": "🤫", "difficulty_icon": "show_chart", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Tabs", "default_bpm": "106", "wiki_link": "https://en.wikipedia.org/wiki/The_Sound_of_Silence", "ug_link": "https://tabs.ultimate-guitar.com/tab/simon-garfunkel/the-sound-of-silence-tabs-58376", "youtube_link": "https://www.youtube.com/results?search_query=sound+of+silence+guitar+tutorial"},
    {"title": "Mrs. Robinson", "artist": "Simon & Garfunkel", "genre": "Folk", "difficulty": "Intermediate", "icon": "👩", "difficulty_icon": "show_chart", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "170", "wiki_link": "https://en.wikipedia.org/wiki/Mrs._Robinson", "ug_link": "https://tabs.ultimate-guitar.com/tab/simon-garfunkel/mrs-robinson-chords-43024", "youtube_link": "https://www.youtube.com/results?search_query=mrs+robinson+guitar+tutorial"},
    {"title": "Fast Car", "artist": "Tracy Chapman", "genre": "Folk", "difficulty": "Intermediate", "icon": "🚗", "difficulty_icon": "show_chart", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "104", "wiki_link": "https://en.wikipedia.org/wiki/Fast_Car", "ug_link": "https://tabs.ultimate-guitar.com/tab/tracy-chapman/fast-car-chords-17658", "youtube_link": "https://www.youtube.com/results?search_query=fast+car+guitar+tutorial"},
    {"title": "No Woman, No Cry", "artist": "Bob Marley", "genre": "Reggae", "difficulty": "Beginner", "icon": "🇯🇲", "difficulty_icon": "trending_flat", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "78", "wiki_link": "https://en.wikipedia.org/wiki/No_Woman,_No_Cry", "ug_link": "https://tabs.ultimate-guitar.com/tab/bob-marley/no-woman-no-cry-chords-10948", "youtube_link": "https://www.youtube.com/results?search_query=no+woman+no+cry+guitar+tutorial"},
    {"title": "Three Little Birds", "artist": "Bob Marley", "genre": "Reggae", "difficulty": "Beginner", "icon": "🐦", "difficulty_icon": "trending_flat", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "74", "wiki_link": "https://en.wikipedia.org/wiki/Three_Little_Birds", "ug_link": "https://tabs.ultimate-guitar.com/tab/bob-marley/three-little-birds-chords-11075", "youtube_link": "https://www.youtube.com/results?search_query=three+little+birds+guitar+tutorial"},
    {"title": "Redemption Song", "artist": "Bob Marley", "genre": "Reggae", "difficulty": "Beginner", "icon": "✊", "difficulty_icon": "trending_flat", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "116", "wiki_link": "https://en.wikipedia.org/wiki/Redemption_Song", "ug_link": "https://tabs.ultimate-guitar.com/tab/bob-marley/redemption-song-chords-11035", "youtube_link": "https://www.youtube.com/results?search_query=redemption+song+guitar+tutorial"},
    {"title": "Shape of You", "artist": "Ed Sheeran", "genre": "Pop", "difficulty": "Beginner", "icon": "➗", "difficulty_icon": "trending_flat", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "96", "wiki_link": "https://en.wikipedia.org/wiki/Shape_of_You", "ug_link": "https://tabs.ultimate-guitar.com/tab/ed-sheeran/shape-of-you-chords-1928437", "youtube_link": "https://www.youtube.com/results?search_query=shape+of+you+guitar+tutorial"},
    {"title": "Perfect", "artist": "Ed Sheeran", "genre": "Pop", "difficulty": "Beginner", "icon": "❤️", "difficulty_icon": "trending_flat", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "95", "wiki_link": "https://en.wikipedia.org/wiki/Perfect_(Ed_Sheeran_song)", "ug_link": "https://tabs.ultimate-guitar.com/tab/ed-sheeran/perfect-chords-1956589", "youtube_link": "https://www.youtube.com/results?search_query=perfect+ed+sheeran+guitar+tutorial"},
    {"title": "Thinking Out Loud", "artist": "Ed Sheeran", "genre": "Pop", "difficulty": "Intermediate", "icon": "💭", "difficulty_icon": "show_chart", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "79", "wiki_link": "https://en.wikipedia.org/wiki/Thinking_Out_Loud", "ug_link": "https://tabs.ultimate-guitar.com/tab/ed-sheeran/thinking-out-loud-chords-1486860", "youtube_link": "https://www.youtube.com/results?search_query=thinking+out+loud+guitar+tutorial"},
    {"title": "All of Me", "artist": "John Legend", "genre": "Pop", "difficulty": "Intermediate", "icon": "🎹", "difficulty_icon": "show_chart", "instrument": "Piano", "instrument_icon": "piano", "genre_icon": "album", "tab_type": "Piano Chords", "default_bpm": "63", "wiki_link": "https://en.wikipedia.org/wiki/All_of_Me_(John_Legend_song)", "ug_link": "https://tabs.ultimate-guitar.com/tab/john-legend/all-of-me-chords-1415956", "youtube_link": "https://www.youtube.com/results?search_query=all+of+me+piano+tutorial"},
    {"title": "Someone Like You", "artist": "Adele", "genre": "Pop", "difficulty": "Intermediate", "icon": "🎤", "difficulty_icon": "show_chart", "instrument": "Piano", "instrument_icon": "piano", "genre_icon": "album", "tab_type": "Piano Chords", "default_bpm": "67", "wiki_link": "https://en.wikipedia.org/wiki/Someone_Like_You_(Adele_song)", "ug_link": "https://tabs.ultimate-guitar.com/tab/adele/someone-like-you-chords-1006751", "youtube_link": "https://www.youtube.com/results?search_query=someone+like+you+piano+tutorial"},
    {"title": "Rolling in the Deep", "artist": "Adele", "genre": "Pop", "difficulty": "Intermediate", "icon": "🌊", "difficulty_icon": "show_chart", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "105", "wiki_link": "https://en.wikipedia.org/wiki/Rolling_in_the_Deep", "ug_link": "https://tabs.ultimate-guitar.com/tab/adele/rolling-in-the-deep-chords-1002880", "youtube_link": "https://www.youtube.com/results?search_query=rolling+in+the+deep+guitar+tutorial"},
    {"title": "Riptide", "artist": "Vance Joy", "genre": "Indie", "difficulty": "Beginner", "icon": "🌊", "difficulty_icon": "trending_flat", "instrument": "Ukulele", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Ukulele Chords", "default_bpm": "100", "wiki_link": "https://en.wikipedia.org/wiki/Riptide_(Vance_Joy_song)", "ug_link": "https://tabs.ultimate-guitar.com/tab/vance-joy/riptide-chords-1234320", "youtube_link": "https://www.youtube.com/results?search_query=riptide+ukulele+tutorial"},
    {"title": "I'm Yours", "artist": "Jason Mraz", "genre": "Pop", "difficulty": "Beginner", "icon": "😊", "difficulty_icon": "trending_flat", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "76", "wiki_link": "https://en.wikipedia.org/wiki/I%27m_Yours_(Jason_Mraz_song)", "ug_link": "https://tabs.ultimate-guitar.com/tab/jason-mraz/im-yours-chords-373896", "youtube_link": "https://www.youtube.com/results?search_query=im+yours+guitar+tutorial"},
    {"title": "Hey Soul Sister", "artist": "Train", "genre": "Pop", "difficulty": "Beginner", "icon": "🚂", "difficulty_icon": "trending_flat", "instrument": "Ukulele", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Ukulele Chords", "default_bpm": "97", "wiki_link": "https://en.wikipedia.org/wiki/Hey,_Soul_Sister", "ug_link": "https://tabs.ultimate-guitar.com/tab/train/hey-soul-sister-chords-884813", "youtube_link": "https://www.youtube.com/results?search_query=hey+soul+sister+ukulele+tutorial"},
    {"title": "Counting Stars", "artist": "OneRepublic", "genre": "Pop", "difficulty": "Intermediate", "icon": "⭐", "difficulty_icon": "show_chart", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "122", "wiki_link": "https://en.wikipedia.org/wiki/Counting_Stars", "ug_link": "https://tabs.ultimate-guitar.com/tab/onerepublic/counting-stars-chords-1233464", "youtube_link": "https://www.youtube.com/results?search_query=counting+stars+guitar+tutorial"},
    {"title": "Radioactive", "artist": "Imagine Dragons", "genre": "Alternative", "difficulty": "Beginner", "icon": "☢️", "difficulty_icon": "trending_flat", "instrument": "Guitar", "instrument_icon": "music_note", "genre_icon": "album", "tab_type": "Guitar Chords", "default_bpm": "136", "wiki_link": "https://en.wikipedia.org/wiki/Radioactive_(Imagine_Dragons_song)", "ug_link": "https://tabs.ultimate-guitar.com/tab/imagine-dragons/radioactive-chords-1171909", "youtube_link": "https://www.youtube.com/results?search_query=radioactive+guitar+tutorial"}
]

base_dir = r"c:\Users\matti\OneDrive\Documents\Code\thesheetmusicdirectory.github.io"
template_path = os.path.join(base_dir, "song_template.html")
content_path = os.path.join(base_dir, "content.html")

# Helper to create filename from title
def create_filename(title):
    return re.sub(r'[^a-z0-9]', '_', title.lower()).strip('_') + ".html"

def create_song_id(title):
    return re.sub(r'[^a-z0-9]', '', title.lower())

def create_song_page(template_path, song_data, output_path):
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Placeholder tab content
    tab_content = f"""
{song_data['title']} - {song_data['artist']}
{'-' * (len(song_data['title']) + len(song_data['artist']) + 3)}

Difficulty: {song_data['difficulty']}
Tuning: Standard

[Intro]
(Tab content coming soon...)

[Verse 1]
(Tab content coming soon...)

[Chorus]
(Tab content coming soon...)

"""
    
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
        '{{SONG_ID}}': create_song_id(song_data['title']),
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

def update_content_html(content_path, new_songs):
    with open(content_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the songs-grid div
    grid_start = content.find('class="songs-grid" id="songsGrid">')
    if grid_start == -1:
        print("❌ Could not find songs-grid in content.html")
        return
    
    # We want to append new songs at the end of the grid, but before the closing div of the grid.
    # The grid ends with the closing </div> of the section.
    # A safer way is to find the last </a> tag in the grid and append after it.
    
    # Let's find the closing tag of the grid.
    # Since we know the structure, we can look for the closing </div> that matches the grid.
    # But regex is tricky with nested divs.
    
    # Alternatively, we can insert after the last </a> tag that has class "song-card"
    last_card_end = content.rfind('</a>')
    if last_card_end == -1:
         print("❌ Could not find any song cards in content.html")
         return
         
    # We need to be careful not to insert after footer links.
    # The grid is inside <div class="songs-grid" id="songsGrid"> ... </div>
    # Let's find the end of that specific div.
    
    # We can split the content by the grid ID
    parts = content.split('class="songs-grid" id="songsGrid">')
    if len(parts) != 2:
        print("❌ Error parsing content.html")
        return
        
    pre_grid = parts[0] + 'class="songs-grid" id="songsGrid">'
    grid_content_and_rest = parts[1]
    
    # Now we need to find where the grid ends.
    # We can count divs to find the matching closing tag, or just assume the indentation.
    # Looking at the file, the grid seems to end before </div>\n        </div>\n    </section>
    
    # Let's try to find the last </a> inside the grid section.
    # We can search for the next </div> that closes the grid.
    # Since the grid contains <a> tags, we can look for the sequence </a>\n            </div>
    
    # A simple approach: Generate the HTML for new songs and insert it before the closing </div> of the grid.
    # We can assume the grid closes with `            </div>\n        </div>\n    </section>`
    
    # Let's construct the HTML for the new songs
    new_songs_html = "\n"
    for song in new_songs:
        filename = create_filename(song['title'])
        html = f"""
                <!-- {song['artist']} Songs -->
                <a href="{filename}" class="song-card" data-genre="{song['genre'].lower()}">
                    <div class="song-image">
                        <span class="material-icons" style="font-size: 64px; opacity: 0.8;">{song['instrument_icon']}</span>
                    </div>
                    <div class="song-content">
                        <h3 class="song-title">{song['title']}</h3>
                        <p class="song-artist">{song['artist']}</p>
                        <div class="song-meta">
                            <span class="material-icons" style="font-size: 18px;">{song['difficulty_icon']}</span>
                            <span>{song['difficulty']}</span>
                        </div>
                        <div class="song-btn">View Tab</div>
                    </div>
                </a>
"""
        new_songs_html += html

    # Now insert it.
    # We look for the closing of the grid.
    # The file ends with:
    #             </div>
    #         </div>
    #     </section>
    
    # We can replace `            </div>\n        </div>\n    </section>` with `new_songs_html +             </div>\n        </div>\n    </section>`
    # But we need to be careful about whitespace.
    
    # Let's try to find the last </a> in the file, which should be the last song card (ignoring footer links for a moment).
    # Actually, footer links are in <footer>.
    
    # Let's use a marker. The grid is inside <div class="songs-grid" id="songsGrid">
    # We can insert right before the closing </div> of that div.
    # Since we can't easily parse the DOM, let's look for the text `</div>` that follows the last song card.
    
    # Let's try to insert before the last `</div>` that is inside the `container` div which is inside `search-section`.
    
    # Better yet, let's just append to the end of the innerHTML of `songs-grid`.
    # We can use regex to find the closing tag of `songs-grid`.
    # It's likely the `</div>` that is followed by `        </div>` and `    </section>`.
    
    pattern = r'(class="songs-grid" id="songsGrid">.*?)(\s+</div>\s+</div>\s+</section>)'
    
    match = re.search(pattern, content, re.DOTALL)
    if match:
        # We found the grid and its end.
        # But wait, the regex `.*?` is non-greedy, it might stop too early if there are nested divs?
        # The song cards don't have nested divs that look like `</div>\n        </div>\n    </section>`.
        # So this should be safe.
        
        # Actually, let's just replace the closing tag sequence.
        replacement = r'\1' + new_songs_html + r'\2'
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        with open(content_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("✅ Updated content.html with new songs")
    else:
        print("❌ Could not safely insert new songs into content.html")


if __name__ == "__main__":
    # 1. Create song pages
    for song in new_songs:
        filename = create_filename(song['title'])
        output_path = os.path.join(base_dir, filename)
        create_song_page(template_path, song, output_path)
    
    # 2. Update content.html
    update_content_html(content_path, new_songs)
