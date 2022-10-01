import base64
path = r'path-to-file' # need to replace with function parameters
with open(path,'r') as f:
    x= base64.b64encode(f.read())

print(x)
