import numpy as np
from PIL import Image, ImageFont, ImageDraw
from nltk.book import text7
import h5py
from aux_functions import downsample_letter

Nwords = len(text7)
text = text7[0:Nwords]
store_directory = './wall_street/'

# Define the font
font_source = './fonts/secrcode.ttf'
# font_source = './Cocomat Ultralight-trial.ttf'
font_source = './fonts/Chunk.ttf'

# The 100 is the pixels, the 256 is the color, 1 is for only one pixel
pixels = 20
coord_x = 2
coord_y = 2
size = 20

font = ImageFont.truetype(font=font_source, size=size)

# Parameters
space = True
save_image = False
to_list = True
downsample = False
renormalize = False
number_format = np.int8
number_format = np.float

counter = 0
image_list = []
letters = []

for word in text:
    # Go through the low caps version of the word
    for letter in word.lower():
        counter += 1
        # Append letter to list\
        letters.append(letter)
        # Create the image and draw the letter
        img = Image.new('1', (pixels, pixels), 256)
        d = ImageDraw.Draw(img)
        d.text((coord_x, coord_y), letter, font=font)

        if save_image:
            img.save(store_directory + str(counter) + '.png')

        if to_list:
            pix = np.array(img.getdata()).reshape(img.size[0], img.size[1])
            if downsample:
                pix = downsample_letter(pix, 40, renormalize)
            image_list.append(pix)

    # Add a space
    if space:
        counter += 1
        # Append letter to list
        letters.append(' ')
        # Create the image and draw the letter
        img = Image.new('1', (pixels, pixels), 256)
        d = ImageDraw.Draw(img)
        letter = ' '
        d.text((coord_x,coord_y), letter, font=font)

        if save_image:
            img.save(store_directory + str(counter) + '.png')

        if to_list:
            pix = np.array(img.getdata()).reshape(img.size[0], img.size[1])
            if downsample:
                pix = downsample_letter(pix, 40, renormalize)
            image_list.append(pix)

# Transform the list into an array
signal = np.array(image_list)
letters = np.asarray(letters)
print('Data size is', signal.shape)
print('Number of words is', Nwords)

# Save this to a hdf5 data base using a context manager
save_filename = './wall_street_data_small.hdf5'
with h5py.File(save_filename, 'w') as f:
    f['/signal'] = signal

# Save the letters
np.save('./wall_street_letters.npy', letters)
