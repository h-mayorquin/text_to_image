from PIL import ImageDraw
from PIL import Image, ImageFont
from string import ascii_lowercase
import numpy as np
import matplotlib.pyplot as plt

store_directory = './alphabet/'

# Defin the font
font_source = './Cocomat Ultralight-trial.ttf'
font_source = './secrcode.ttf'

font = ImageFont.truetype(font=font_source, size=80)

# The 100 is the pixels, the 256 is the color, 1 is for only one pixel
pixels = 100
coord_x = 18
coord_y = 18

for letter in ascii_lowercase:
    img = Image.new('1', (pixels, pixels), 256)
    d = ImageDraw.Draw(img)
    d.text((coord_x, coord_y), letter, font=font)
    img.save(store_directory + letter + '.png')

for i in range(0, 10):
    letter = str(i)
    img = Image.new('1', (pixels, pixels), 256)
    d = ImageDraw.Draw(img)
    d.text((coord_x, coord_y), letter, font=font)
    img.save(store_directory + letter + '.png')

# I just need now to transform this into numpy arrays in
#  order to operate with them
pix = np.array(img.getdata()).reshape(img.size[0], img.size[1])

# Note that you can also plot the img object directly
#plt.matshow(pix)
#plt.show()
