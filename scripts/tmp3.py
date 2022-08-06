"""
Auto rename the json file of each palette
given the palette's name.
"""

import os
import json

palettes = os.listdir('./palettes')

items = []

for pal in palettes:
    name = json.load(open(f'./palettes/{pal}', 'r'))['name']
    
    name = name.replace(' ', '-').lower()
    
    items.append((pal, f'{name}.json'))


for old, new in items:
    os.rename(f'./palettes/{old}', f'./palettes/{new}')
    print(f'renamed {old}')