import os

from PIL import Image, ImageEnhance
import numpy as np


if __name__ == '__main__':
    image = Image.new("RGBA",(34*64,34*16))
    for tile in range(len(os.listdir("output"))):
        tilename = os.listdir("output")[tile]
        for edge in range(len(os.listdir("output/" + tilename))):
            edgename = os.listdir("output/" + tilename)[edge]
            image.paste(Image.open("output/" + str(tile//8) + "_" + str(tile%8) + "/" + str(edge) + ".png"),(tile*34, edge*34))
    image.save("tileset.png","PNG")
