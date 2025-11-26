import os, re

ROOT = r"c:\\Users\\matti\\OneDrive\\Documents\\Code\\thesheetmusicdirectory.github.io"
CONTENT_PATH = os.path.join(ROOT, "content.html")

# Read content.html
with open(CONTENT_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Pattern to find song card blocks (anchor tags with href)
pattern = re.compile(r'(<a\s+href=\"(?P<href>[^\"]+\.html)\"[^>]*>.*?</a>)', re.DOTALL)

def file_exists(href):
    return os.path.isfile(os.path.join(ROOT, href))

new_blocks = []
for match in pattern.finditer(content):
    href = match.group('href')
    if file_exists(href):
        new_blocks.append(match.group(0))
    else:
        # Skip block for missing file
        pass

# Reconstruct the songs-grid section
# Find the start and end of the grid
grid_start = content.find('<div class="songs-grid" id="songsGrid">')
if grid_start == -1:
    raise ValueError('songs-grid div not found')
grid_end = content.find('</section>', grid_start)
if grid_end == -1:
    raise ValueError('section end not found')
# Build new grid content
new_grid = '<div class="songs-grid" id="songsGrid">\n' + "\n".join(new_blocks) + '\n</div>'
# Replace old grid with new grid
new_content = content[:grid_start] + new_grid + content[grid_end:]

# Write back
with open(CONTENT_PATH, "w", encoding="utf-8") as f:
    f.write(new_content)
print(f"Updated content.html, kept {len(new_blocks)} song cards.")
