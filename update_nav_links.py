import os
import re

def update_nav_links(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # 1. Replace Profile link if it exists
            if 'href="profile.html"' in content:
                content = content.replace('href="profile.html"', 'href="account.html"')
                content = re.sub(r'(<a href="account\.html"[^>]*>)\s*Profile\s*(</a>)', r'\1Account\2', content)
            
            # 2. Add Account link if it doesn't exist and we are in a page with a header-nav
            if 'class="header-nav"' in content and 'href="account.html"' not in content:
                # Find the closing div of header-nav
                # We assume the structure is <div class="header-nav"> ... </div>
                # We want to insert <a href="account.html" class="nav-link">Account</a> before the closing </div>
                
                # Regex to find the content inside header-nav
                # This is a bit risky with regex, but given the consistent formatting it should work.
                # We look for the last </a> inside header-nav and append after it.
                
                pattern = r'(<div class="header-nav">.*?)(</div>)'
                
                def add_link(match):
                    inner_content = match.group(1)
                    closing_tag = match.group(2)
                    
                    # Check if we already have it (double check)
                    if 'account.html' in inner_content:
                        return match.group(0)
                        
                    # Add the link
                    # Determine if we need a newline or space
                    return f'{inner_content}\n            <a href="account.html" class="nav-link">Account</a>\n        {closing_tag}'
                
                content = re.sub(pattern, add_link, content, flags=re.DOTALL)
                
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated: {filename}")
            else:
                print(f"No changes needed: {filename}")

if __name__ == "__main__":
    base_dir = r"c:\Users\matti\OneDrive\Documents\Code\thesheetmusicdirectory.github.io"
    update_nav_links(base_dir)
