from PIL import Image
import os

directory = './HEICS'
files = [f for f in os.listdir(directory) if f.endswith('.heic') or f.endswith('.heif')]


for filename in files:
    image = Image.open(os.path.join(directory, filename))
    image.convert('RGB').save(os.path.join(directory, os.path.splitext(filename)[0] + '.jpg'))
    