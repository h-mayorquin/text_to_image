import numpy as np
from scipy.misc import imresize

# Downsampling
def downsample_letter(image, size, renormalize=True):
    """
    A convenience function to downsample an image. Where
    size is the new size if we renormalize them to two
    values if renormalize is equal to two.
    """
    downsample = imresize(image, size=(size, size))
    max_value = np.max(downsample)
    min_value = np.min(downsample)

    if renormalize:
        downsample[downsample <= 127 ] = min_value
        downsample[downsample > 127] = max_value

    return downsample
