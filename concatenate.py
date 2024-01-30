import os

from PIL import Image, ImageEnhance
import numpy as np


if __name__ == '__main__':
    image = Image.new("RGBA",(18*64,18*64))
    for tile in range(len(os.listdir("output"))):
        tilename = os.listdir("output")[tile]
        for edge in range(len(os.listdir("output/" + tilename))):
            edgename = os.listdir("output/" + tilename)[edge]
            image.paste(Image.open("output/" + str(tile//16) + "_" + str(tile%16) + "/" + str(edge) + ".png"),(((tile%64)*18), edge*18+16*18*(tile//64)))
    image.save("tileset.png","PNG")
