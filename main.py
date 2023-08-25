from Module import HanulIMG as HIMG
from time import time
from PIL import Image
import os
import asyncio

#PIL setting
Image.MAX_IMAGE_PIXELS = None


HIMG.save("SHI","pxfuel (1).jpg")

obefore,oafter = None,None

before = time()
img = HIMG.load("SHI.HIMG")
after =  time()

async def sub1():
    await asyncio.sleep(30)
    

async def sub2():
    global obefore,oafter
    obefore = time()
    img.show()
    oafter =  time()
    
async def main():
    abefore = time()
    
    await asyncio.gather(
        sub1(),
        sub2()
    )
    
    aafter = time()
    print("load time:{time}\nopen time:{otime}\nall time:{atime}".format(time=after-before,otime=oafter-obefore,atime=aafter-abefore))

asyncio.run(main())