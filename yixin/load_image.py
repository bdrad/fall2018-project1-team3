import os
import sys
import pydicom
from skimage.transform import resize

def load_and_resize(filename, size = None):
    """
    Take in the filepath of a .dcm file, load it into a numpy 2d array and resize it. 
    Args:
        filename (string): the filepath
        size (tuple): the size to resize to, example: (x, y)
    Return: 
        [the (resized) image, pathology]
    """
    ds = pydicom.dcmread(filename)

    image = ds.pixel_array
    if size != None:
        image = resize(image, size)
    return image

if __name__== "__main__" :
    if len(sys.argv) < 2:
        print("please enter file path")
    else:
        # parse args
        filename = sys.argv[1]
        size = None
        if len(sys.argv) == 4:
            size = (sys.argv[2], sys.argv[3])
        print(load_and_resize(filename, size))
