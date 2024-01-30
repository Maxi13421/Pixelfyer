from PIL import Image, ImageEnhance
import cv2
import numpy as np


def Get(imagename):
    im = cv2.imread(imagename)
    imarray = im.astype(np.uint8)
    list = np.array([[-1, -1, -1]])
    for x in range(imarray.shape[0]):
        for y in range(imarray.shape[1]):
            if not (np.any(np.all(imarray[x][y] == list, axis=1))):
                list = np.append(list, [imarray[x][y]], axis=0)
    # print(list[1:].reshape((1,17,3)))
    # cv2.imwrite("PaletteAsteroid.png",(list[1:].reshape((1,17,3))).astype(np.uint8))
    newlist = list[1:]
    newlistsorted = sorted(newlist.tolist(),
                           key=lambda color: -(color[0] * 0.0722 + color[1] * 0.7152 + color[2] * 0.2126))
    print(newlistsorted)
    palettedec = [hex(int(a[2] * 256 * 256 + a[1] * 256 + a[0])) for a in newlistsorted]
    out = ""
    for a in palettedec:
        out+=a.split("x")[1] +","
    return out[:-1]

if __name__ == '__main__':
    print(Get("Saturn185x8017col.png"))
