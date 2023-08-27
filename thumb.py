from Module.HanulIMG import MakeThumbnail
from PIL import Image

from os import path

def thumb(imgname)->str:
    print(path.abspath(__file__))
    with Image.open(f'static/images/{imgname}','r') as img:
        thumb = MakeThumbnail(img)
        try:
            with open(f'static/.thumbnails/{imgname}','x') as file:
                pass
        except FileExistsError:
            pass
        else:
            thumb.save(f'static/.thumbnails/{imgname}')
    return f'../static/.thumbnails/{imgname}'
            