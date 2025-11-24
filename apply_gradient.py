import os
import re

# List of files to update (excluding song pages which are already done)
files_to_update = [
    'content.html',
    'videos.html',
    'account.html',
    'privacy.html',
    'terms.html',
    'comingsoon.html',
    '404.html',
    '404-2.html'
]

base_dir = r'c:\Users\matti\OneDrive\Documents\Code\thesheetmusicdirectory.github.io'

for filename in files_to_update:
    filepath = os.path.join(base_dir, filename)
    
    if not os.path.exists(filepath):
        print(f"⚠️  Skipping {filename} (not found)")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add gradient background to body
    content = re.sub(
        r'(body\s*\{[^}]*background:\s*)(#fff|var\(--bg-color\)|white)([^}]*\})',
        r'\1linear-gradient(135deg, #f8f9fa 0%, #e8eaed 100%)\3\n            min-height: 100vh;',
        content,
        flags=re.DOTALL
    )
    
    # Make hero shapes fixed position if they exist
    content = re.sub(
        r'(\.hero-shape\s*\{[^}]*position:\s*)absolute',
        r'\1fixed',
        content
    )
    
    # Add z-index to hero shapes if missing
    if '.hero-shape' in content and 'z-index' not in content:
        content = re.sub(
            r'(\.hero-shape\s*\{[^}]*)(animation:[^;]+;)',
            r'\1\2\n            z-index: 0;',
            content
        )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Updated: {filename}")

print("\n✅ All pages updated with gradient background!")
