from PIL import Image


import glob, os, sys
from PIL import Image

folder = 'C:/Users/39392/Desktop/dataset/'

for filepath in glob.iglob(os.path.join(folder, '*.jpg')):
    image = Image.open(filepath).convert('RGB')
    new_filepath = os.path.splitext(filepath)[0] + '.jpg'
    image.save(new_filepath)