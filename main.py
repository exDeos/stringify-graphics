import base64

def convert_img(path_to_img_file):
    with open(path_to_img_file,'r') as f:
        x= base64.b64encode(f.read())
    return x

path_to_file = r'path-to-file' # need to replace with function parameters

