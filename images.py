from PIL import ImageDraw
from PIL import Image, ImageFont
from string import ascii_lowercase
import numpy as np
import matplotlib.pyplot as plt

store_directory = './alphabet/'

# Defin the font
font = ImageFont.truetype(font='./Cocomat Ultralight-trial.ttf', size=80)

# The 100 is the pixels, the 256 is the color, 1 is for only one pixel

for letter in ascii_lowercase:
    img = Image.new('1', (100, 100), 256)
    d = ImageDraw.Draw(img)
    d.text((20, 20), letter, font=font)
    # img = Image.new('1', (200, 100), (255, 255, 255))
    img.save(store_directory + letter + '.png')

# I just need now to transform this into numpy arrays in
#  order to operate with them
pix = np.array(img.getdata()).reshape(img.size[0], img.size[1])

# Note that you can also plot the img object directly
plt.matshow(pix)
plt.show()
