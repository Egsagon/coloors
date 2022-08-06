"""
Parse the palettes in a txt file and save them
into random named files.
"""

import json
from copy import copy
from random import randint

data = open('/home/egsagon/colors/plt/Color_palettes.txt', 'r').read()

base = {
    "name":     "NAME",
    "auth":     "egsagon",
    "desc":     "DESCRIPTION",
}

"""
"com_fg":   "000",
    "fg":       "888",

    "com_acc":  "0f0",
    "accent":   "f00",

    "com_bg":   "f0f",
    "bg":       "fff"
"""

plts = data.split('#')
PALETTE_KEYS = ['com_fg', 'fg', 'com_acc', 'accent', 'com_bg', 'bg']
done = []

for plt in plts:
    parts = plt.split('\n')
    head, cnt = parts[0], parts[1:]
    
    cnt = list(filter(lambda c: c, cnt))
    
    for i, _ in enumerate(cnt):
        cnt[i] = cnt[i].upper()
    
    if len(cnt): done.append(cnt)





# Write
for palette in done:
    cur = copy(base)
    
    for key, value in zip(PALETTE_KEYS, palette):
        cur[key] = value
    
    file = open(f'{randint(0, 1000)}.json', 'w')
    file.write(json.dumps(cur, indent=4))
    file.close()