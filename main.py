import base64

def convert_img(path_to_img_file):
    with open(path_to_img_file,'rb') as f:
        x= base64.b64encode(f.read())
    return x

path_to_file = r'path-to-file' # need to replace with function parameters

from PIL import Image
from io import BytesIO

def make_img(imstr):
    with BytesIO(base64.b64decode(imstr) as f:
        im= Image.open(f)
    return im

# to be added later ?
