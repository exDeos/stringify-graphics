import base64

def convert_img(path_to_img_file):
    with open(path_to_img_file,'rb') as f:
        x= base64.b64encode(f.read())
    return x.decode('utf-8')

path_to_img_file = r'path-to-file' # need to replace with function parameters
imstr= convert_img(path_to_img_file)

from PIL import Image
from io import BytesIO
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['toolbar'] = 'None'

im= Image.open( BytesIO(base64.b64decode(imstr.encode('utf-8'))) )
plt.imshow(im)
plt.axis('off')
plt.show()

# to be added later ?
