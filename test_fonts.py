"""
This script produces the whole alphabet (and all the other symbols for a given font)
for a given corpus. This serves as test for all the font parameters and the font itself.
"""

from PIL import ImageDraw
from PIL import Image, ImageFont
import numpy as np
import matplotlib.pyplot as plt
from random import sample
# from string import ascii_lowercase

# Now we import the particular corpus that we are intested in
from nltk.book import text7 as text
letters = ' '.join(text)
symbols = set(letters)

# Get a dictionary of difficult symbols
difficult_symbols = {' ': 'space', '.':'point', '/':'diagonal'}

store_directory = './alphabet/'

# Define the font
font_directory = './fonts/'
font_name = 'Cocomat Ultralight-trial.ttf'
font_name = 'secrcode.ttf'
font_name = 'Chunk.ttf'
font_name = 'hellovetica.ttf'
font_name = 'arcade.ttf'
font_source = font_directory + font_name

# Now we chose how the image will be layed out
pixels = 10  # Number of pixels 
coord_x = 2  # 
coord_y = 0
size = 15

font = ImageFont.truetype(font=font_source, size=size)

# Go through all the symbols and print them as images
for symbol in symbols:
    # 256 is the color and 1 is only for one pixel
    img = Image.new('1', (pixels, pixels), 256)
    d = ImageDraw.Draw(img)
    d.text((coord_x, coord_y), symbol, font=font)
    if symbol in difficult_symbols:
        symbol = difficult_symbols[symbol]

    name = store_directory + symbol + '.png'
    print('saving name', name)
    img.save(name)


# We also have a function to transform to numpy arrays
def symbol_to_array(symbol, font, pixels, coord_x, coord_y, size):
    """
    Return a numpy array for a given symbol with a given font
    """

    # 256 is the color and 1 is only for one pixel
    img = Image.new('1', (pixels, pixels), 256)
    d = ImageDraw.Draw(img)
    d.text((coord_x, coord_y), symbol, font=font)
    img.save(name)

    numpy_array = np.array(img.getdata()).reshape(img.size[0], img.size[1])

    return numpy_array

# Show random image
shows_random_image = True
if shows_random_image:
    symbol = sample(symbols, 1)[0]
    # symbol = '\\'
    pix = symbol_to_array(symbol, font, pixels, coord_x, coord_y, size)
    plt.matshow(pix)
    plt.show()
