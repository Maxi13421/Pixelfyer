import numpy as np
from PIL import Image

if __name__ == '__main__':
    im = np.asarray(Image.open("tileset.png").convert())
    outputarray = np.ndarray((imarray.shape[0], imarray.shape[1], 4))
    im.