#image_edits.py
from cv2 import imread, COLOR_RGB2GRAY, cvtColor, imwrite
import os
def write_grayscale_image(filepath):
    original_image = imread(filepath)
    grayed_image = cvtColor(original_image, COLOR_RGB2GRAY)
    grayed_filename=os.path.join(os.path.split(filepath)[0],'grayed_'+os.path.split(filepath)[1])
    print(grayed_filename)
    imwrite(grayed_filename, grayed_image) #export grayscaled image
    return grayed_filename