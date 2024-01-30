import os

from PIL import Image, ImageEnhance
import numpy as np

def cutEdges(imagename):
    im = Image.open("MainOutput/" + imagename)
    imarray = np.asarray(im.convert())
    outputarray = np.ndarray((imarray.shape[0], imarray.shape[1], 4))
    os.mkdir("output/" + imagename.split(".")[0])

    for baa in range(16):
        outputarray = np.ndarray((imarray.shape[0], imarray.shape[1], 4))
        for aaa in range(imarray.shape[0]):
            for aab in range(len(imarray[aaa])):

                if (baa % 2 == 1 and aaa <= 9 and aab <= 9 and aaa < (aaa - 10.5) ** 2 + (aab - 10.5) ** 2 > 10.5 ** 2
                        or (baa >> 1) % 2 == 1 and aaa >= 8 and aab <= 9 and aaa < (aaa - 6.5) ** 2 + (
                                aab - 10.5) ** 2 > 10.5 ** 2
                        or (baa >> 2) % 2 == 1 and aaa <= 9 and aab >= 8 and aaa < (aaa - 10.5) ** 2 + (
                                aab - 6.5) ** 2 > 10.5 ** 2
                        or (baa >> 3) % 2 == 1 and aaa >= 9 and aab >= 9 and aaa < (aaa - 6.5) ** 2 + (
                                aab - 6.5) ** 2 > 10.5 ** 2
                ):
                    outputarray[aaa][aab][3] = 0
                else:
                    outputarray[aaa][aab][3] = 255
                outputarray[aaa][aab][0] = imarray[aaa][aab][0]
                outputarray[aaa][aab][1] = imarray[aaa][aab][1]
                outputarray[aaa][aab][2] = imarray[aaa][aab][2]
        output_image = Image.fromarray(np.uint8(outputarray))
        output_image.save("output/" + imagename.split(".")[0] + "/" + str(baa) + ".png")

if __name__ == '__main__':
    os.mkdir("output")
    for name in os.listdir("MainOutput"):
        cutEdges(name)


