from os import listdir, rename

IMGS = listdir('./wallpapers')

i = 0

for img in IMGS:
    print(img)
    
    ext = img.split('.')[-1]
    name = f'{i}.{ext}'
    
    rename(f'./wallpapers/{img}', f'./wallpapers/{name}')

    i += 1