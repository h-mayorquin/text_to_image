from PIL import Image, ImageFont, ImageDraw
from string import ascii_lowercase
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

store_directory = './alphabet/'

# Defin the font
font_source = './Cocomat Ultralight-trial.ttf'
font_source = './secrcode.ttf'

font = ImageFont.truetype(font=font_source, size=80)

# The 100 is the pixels, the 256 is the color, 1 is for only one pixel
pixels = 100
coord_x = 18
coord_y = 18

letter = ascii_lowercase[3]
img = Image.new('1', (pixels, pixels), 256)
d = ImageDraw.Draw(img)
d.text((coord_x, coord_y), letter, font=font)
img.save(store_directory + letter + '.png')

# I just need now to transform this into numpy arrays in
#  order to operate with them
pix = np.array(img.getdata()).reshape(img.size[0], img.size[1])

# Downsampling
def downsample_letter(image, size):
    """
    A convenience function to downsample an image
    """
    downsample = sp.misc.imresize(pix, size=(size, size))
    downsample[downsample < 127 ] = 0
    downsample[downsample > 127] = 255

    return downsample


new_image = downsample_letter(pix, 50)
plt.matshow(new_image)
plt.colorbar()
plt.show()
