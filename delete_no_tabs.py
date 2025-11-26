import os, re

# Directory containing song pages
ROOT_DIR = r"c:\\Users\\matti\\OneDrive\\Documents\\Code\\thesheetmusicdirectory.github.io"

# Regex to capture the content inside the <pre id="tabContent"> tag
PRE_PATTERN = re.compile(r'<pre\s+id=["\']tabContent["\']>(.*?)</pre>', re.DOTALL | re.IGNORECASE)

# Placeholder text that indicates missing tabs
PLACEHOLDER = "(Tab content coming soon...)"

def should_delete(content):
    # Find the <pre> block
    match = PRE_PATTERN.search(content)
    if not match:
        # No tab content block – safe to keep (maybe not a song page)
        return False
    inner = match.group(1).strip()
    # Delete if placeholder present or if inner content is empty
    return not inner or PLACEHOLDER in inner

deleted = []
for dirpath, _, filenames in os.walk(ROOT_DIR):
    for fname in filenames:
        if fname.lower().endswith('.html'):
            path = os.path.join(dirpath, fname)
            with open(path, 'r', encoding='utf-8') as f:
                data = f.read()
            if should_delete(data):
                os.remove(path)
                deleted.append(path)
                print(f"Deleted {path}")

print(f"Total deleted: {len(deleted)}")
