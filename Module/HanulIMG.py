import base64 as _base64
from PIL import Image as _Image

from os import chdir

if __name__ == "__main__":
    from HanulAES import HanulEncrypt as _HanulEncrypt, HanulDecrypt as _HanulDecrypt
else:
    from Module.HanulAES import HanulEncrypt as _HanulEncrypt, HanulDecrypt as _HanulDecrypt
from io import BytesIO as _BytesIO

key = "123"

def ImgFileToB64(fb):
    return _base64.b64encode(fb.read())

def save(savefilename,ImageFileName):
    with open(ImageFileName,"rb") as Imagefile:
        try:
            with open(savefilename+".HIMG","x",encoding="utf8") as file:
                content = ImgFileToB64(Imagefile)
                content = _HanulEncrypt(key,content)
                file.write(content)
        except FileExistsError:
            with open(savefilename+".HIMG","w",encoding="utf8") as file:
                content = ImgFileToB64(Imagefile)
                content = _HanulEncrypt(key,content.decode())
                file.write(content)
        
def load(HImagepath)->_Image.Image:
    try:
        with open(HImagepath,"rb") as file:
            content = _HanulDecrypt(key,file.read())
            content = _base64.b64decode(content)
            return _Image.open(_BytesIO(content))
    except Exception as e:
        raise e

def MakeThumbnail(img:_Image.Image):
    if img.width < 128:
        ImageFake = img.resize((128,int(img.height*128/img.width)))
    elif img.height < 128:
        ImageFake = img.resize((int(img.width*128/img.height),128))
    else:
        if img.width < img.height:
            ImageFake = img.resize((128,int(img.height*128/img.width)))
        elif img.height < img.width:
            ImageFake = img.resize((int(img.width*128/img.height),128))
        else:
            ImageFake = img.resize((128,128))
    return ImageFake.crop((
        int((ImageFake.width-128)/2),
        int((ImageFake.height-128)/2),
        int((ImageFake.width-128)/2+128),
        int((ImageFake.height-128)/2+128)
    ))


if __name__ == "__main__":
    save("Untitled (8)","Untitled (8).png")
    load("Untitled (8).HIMG").show()