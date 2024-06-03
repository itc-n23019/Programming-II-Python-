import sys, re

if len(sys.argv) < 2:
    sys.exit('Usage: sentence_generator.py <src.txt>')

with open(sys.argv[1], 'r') as src_file:
    src_data = src_file.read()

pattern = re.compile(r'(ADJECTIVE|NOUN|VERB|ADVERB)')
while (mo := pattern.search(src_data)):
    repl = input(f'Enter a{"n" if mo.group(1).startswith("A") else ""} {mo.group(1).lower()}: ')
    src_data = src_data.replace(mo.group(1), repl, 1)

print(src_data, end='')

with open(f'{sys.argv[1]}.generated.txt', 'w') as dst_file:
    dst_file.write(src_data)
