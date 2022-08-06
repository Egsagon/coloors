"""
Rename tool for each palette.
"""

import json
from os import listdir, system
from PIL import Image, ImageDraw

file = './palettes/10.json'
PALETTE_KEYS = ['com_fg', 'fg', 'com_acc', 'accent', 'com_bg', 'bg']

palettes = listdir('./palettes')

def display_palette(path):
    data = json.load(open(path, 'r'))
    
    img = Image.new("RGB", (100, 300), 'red')
    draw = ImageDraw.Draw(img)
    for i, key in enumerate(PALETTE_KEYS):
        shape = [0, i * 50, 100, i * 50 + 50]
        draw.rectangle(shape, fill = '#' + data[key])

    draw = ImageDraw.Draw(img)
    img.save('tmp.png')
    

"""
while 1:
    print('# - # - #')
    
    for pal in palettes:
        data = json.load(open(f'./palettes/{pal}', 'r'))
        
        img = Image.new("RGB", (100, 300), 'red')

        draw = ImageDraw.Draw(img)

        for i, key in enumerate(PALETTE_KEYS):
            
            shape = [0, i * 50, 100, i * 50 + 50]
            
            draw.rectangle(shape, fill = '#' + data[key])


        draw = ImageDraw.Draw(img)
        img.save('tmp.png')
        
        system('clear')

        print('name:', data['name'])
        new_name = input('Name: ')
        
        if not new_name: continue
        
        data['name'] = new_name
        
        open(f'./palettes/{pal}', 'w').write(
            json.dumps(data, indent = 4)
        )
"""


display_palette('./palettes/name.json')