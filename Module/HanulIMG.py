import base64 as _base64
from PIL import Image as _Image

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

if __name__ == "__main__":
    save("Untitled (8)","Untitled (8).png")
    load("Untitled (8).HIMG").show()