import os, sys, re

if len(sys.argv) < 2:
    sys.exit('Usage: python findre.py <pattern>')

pattern = re.compile(sys.argv[1])
for filename in filter(lambda f: f.lower().endswith('.txt'), os.listdir('./')):
    with open(filename, 'r', encoding='utf-8') as txt_file:
        for line in txt_file:
            if pattern.search(line):
                print(f'{filename}: {line}', end='')
