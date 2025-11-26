import os, re

def delete_empty_tab_pages(root_dir):
    pattern = re.compile(r'<pre id="tabContent">\s*(.*?)\s*</pre>', re.DOTALL | re.IGNORECASE)
    for dirpath, _, filenames in os.walk(root_dir):
        for fname in filenames:
            if fname.lower().endswith('.html'):
                path = os.path.join(dirpath, fname)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                match = pattern.search(content)
                if match:
                    inner = match.group(1).strip()
                    if not inner:  # empty or only whitespace
                        os.remove(path)
                        print(f"Deleted {path}")

if __name__ == '__main__':
    root = r"c:\\Users\\matti\\OneDrive\\Documents\\Code\\thesheetmusicdirectory.github.io"
    delete_empty_tab_pages(root)
