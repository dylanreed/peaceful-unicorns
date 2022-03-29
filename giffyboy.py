import PIL
import imageio
from PIL import Image
import os, sys


path = "/Users/nervousmini/Documents/GitHub/peaceful-unicorns/images/"

resize_ratio = 0.5  # where 0.5 is half size, 2 is double size

def resize_aspect_fit():
    dirs = os.listdir(path)
    for item in dirs:
        if item == '.png':
            continue
        if os.path.isfile(path+item):
            image = Image.open(path+item)
            file_path, extension = os.path.splitext(path+item)

            new_image_height = int(image.size[0] / (1/resize_ratio))
            new_image_length = int(image.size[1] / (1/resize_ratio))

            image = image.resize((new_image_height, new_image_length), Image.ANTIALIAS)
            image.save("/Users/nervousmini/Documents/GitHub/peaceful-unicorns/images/resized/" + item + "_small" + extension, 'JPEG', quality=90)


resize_aspect_fit()



small_dir = '/Users/nervousmini/Documents/GitHub/peaceful-unicorns/images/resized'
images = []
for file_name in sorted(os.listdir(small_dir)):
    if file_name.endswith('.png'):
        file_path = os.path.join(small_dir, file_name)
        images.append(imageio.imread(file_path))
imageio.mimsave('/Users/nervousmini/Documents/GitHub/peaceful-unicorns/gif/movie.gif', images, fps = 3)
