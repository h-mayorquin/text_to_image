"""
This transforms all the text on the wall street corpus on the
nltk package to images.
"""
import numpy as np
from PIL import Image, ImageFont, ImageDraw
import h5py

# Now we import the particular corpus that we are intested in
from nltk.book import text7 as text

# General parameters
lowercase = True  # Makes all the letter lowercase

Nwords = len(text)
# Nwords = 20
text = text[0:Nwords]
letters = ' '.join(text)

# Get letters to a list
if lowercase:
    letters = [letter.lower() for letter in letters]
else:
    letters = [letter for letter in letters]

Nletters = len(letters)

store_directory = './wall_street/'

# Define the font
font_directory = './fonts/'
font_name = 'arcade.ttf'
font_source = font_directory + font_name

pixels = 10
coord_x = 2
coord_y = 0
size = 15

font = ImageFont.truetype(font=font_source, size=size)

# Parameters for the run
save_image = True  # Stores images in the store_directory
counter = 0
image_list = []

for letter in letters:
    if letter != ' ':
        # 256 is the color and 1 is only for one pixel
        img = Image.new('1', (pixels, pixels), 256)
        d = ImageDraw.Draw(img)
        d.text((coord_x, coord_y), letter, font=font)

        if save_image:
            img.save(store_directory + str(counter) + '.png')
            counter += 1

        pix = np.array(img.getdata()).reshape(img.size[0], img.size[1])
        image_list.append(pix)

# Transform the list into an array
signal = np.array(image_list)
letters_array = np.asarray(letters)
print('Data size is', signal.shape)
print('Number of words is', Nwords)
print('Number of letters', Nletters)

# Save this to a hdf5 data base using a context manager
save_filename = './wall_street_data.hdf5'
with h5py.File(save_filename, 'w') as f:
    f['/signal'] = signal

# Save the letters
np.save('./wall_street_letters.npy', letters_array)
