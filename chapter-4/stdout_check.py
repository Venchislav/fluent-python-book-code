import sys
from unicodedata import name

print(sys.version)
print()
print('sys.stdout.isatty():', sys.stdout.isatty())
print('sys.stdout.encoding:', sys.stdout.encoding)
print()

test_chars = [
    '\N{HORIZONTAL ELLIPSIS}', # is in cp1252, but not in cp437
    '\N{INFINITY}', # is in cp437, but not in cp1252
    '\N{CIRCLED NUMBER FORTY TWO}', # isn't in cp437, and cp1252
]
for char in test_chars:
    print(f'Trying to output {name(char)}:')
    print(char)