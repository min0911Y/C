from os import walk
from os.path import join as pjoin
for path, _, files in walk('.'):
    for file in files:
        if not file.endswith('.md'):
            with open(pjoin(path, file) + '.md', 'w') as f:
                f.write(f"[{file}](./{file} ':include')")
