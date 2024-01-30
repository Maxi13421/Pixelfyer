import sys
import time

import cv2
import numpy as np
from PIL import Image
import colour

import GetHexCodesFromPicture
import sortPalette


def find(numberColours, picture):
    palette = np.full((1,numberColours,3),0,np.float32)
    paletteout = np.full((1,numberColours,3),0,np.float32)


    im = cv2.imread(picture)
    imarray = cv2.cvtColor(im.astype(np.float32)/255, cv2.COLOR_BGR2Lab)
    oneColouredPictures =  [np.full(imarray.shape,0) for i in range(numberColours)]
    p_img = Image.new('P', (16, 32))
    for aaa in range(numberColours):
        bestrgb = np.ndarray((3,))
        bestvalue = 10000000000
        for r in range(4):
            palette[0][aaa][0] = r*64+32
            for g in range(4):
                print(str(aaa) + " " +str(r) + " " +str(g) + " ")
                palette[0][aaa][1] = g*64+32
                for b in range(4):
                    palette[0][aaa][2] = b*64+32

                    palettelab =  paletteout.copy()
                    colournp = np.ndarray((1,1,3))
                    colournp[0][0][0] = r*64+32
                    colournp[0][0][1] = g*64+32
                    colournp[0][0][2] = b*64+32
                    colourlab= cv2.cvtColor(colournp.astype(np.float32)/256, cv2.COLOR_RGB2Lab)[0][
                        0]


                    palettelab[0][aaa][0],palettelab[0][aaa][1],palettelab[0][aaa][2] = colourlab[0],colourlab[1],colourlab[2]

                    sum = 0
                    for x in range(len(imarray)):
                        for y in range(len(imarray[x])):
                            closestColour = 0
                            timee = time.perf_counter_ns()
                            closestDif = colour.delta_E([imarray[x][y]],[palettelab[0][0]])
                            print(time.perf_counter_ns() - timee)
                            #print(str(r) + " " + str(g) + " " + str(b) + " " + str(imarray[x][y]) + " "+ str(colour.delta_E([imarray[x][y]],[palettelab[0][0]])))
                            for i in range(1, aaa+1):
                                dif=colour.delta_E([imarray[x][y]],[palettelab[0][i]])
                                #print(colour.delta_E([imarray[x][y]],[palettelab[0][i]]))
                                if(dif< closestDif[0]):
                                    closestDif = dif
                                    closestColour = i
                            sum += closestDif
                    if(sum< bestvalue):
                        bestvalue = sum
                        bestrgb[0],bestrgb[1],bestrgb[2] = palettelab[0][aaa][0],palettelab[0][aaa][1],palettelab[0][aaa][2]
        print(bestvalue)
        print(bestrgb)
        paletteout[0][aaa][0],paletteout[0][aaa][1],paletteout[0][aaa][2] = bestrgb[0],bestrgb[1],bestrgb[2]
        print(paletteout)


    print(paletteout)

    return paletteout

def findEfficient(numberIterations, picture, numbercolours):
    palette = np.full((1, numberIterations, 3), 0, np.float32)
    paletteout = np.full((1, numberIterations, 3), 0, np.float32)


    im = cv2.imread(picture)
    imarray = cv2.cvtColor(im.astype(np.float32)/255, cv2.COLOR_BGR2Lab)
    oneColouredPictures =  [np.full(imarray.shape,0.0).astype(np.float32) for i in range(numberIterations)]
    oneColouredPictureDifferences = [np.full((imarray.shape[0],imarray.shape[1]), 0).astype(np.float32) for i in range(numberIterations)]
    #oneColouredPictureDifferencesMap = {}
    oneColouredPictureBestDifferences = [np.full((imarray.shape[0],imarray.shape[1]), 0).astype(np.float32) for i in range(numberIterations)]
    for aaa in range(numberIterations):
        bestlab = np.ndarray((3,))
        bestpalette = np.ndarray((3,))
        bestvalue = 10000000000
        for r in range(16):
            palette[0][aaa][0] = r*16+8
            for g in range(16):
                #print(str(aaa) + " " + str(r) + " " + str(g) + " ")
                palette[0][aaa][1] = g*16+8
                for b in range(16):
                    palette[0][aaa][2] = b*16+8

                    palettelab = paletteout.copy()
                    colournp = np.ndarray((1,1,3))
                    colournp[0][0][0] = palette[0][aaa][0]
                    colournp[0][0][1] = palette[0][aaa][1]
                    colournp[0][0][2] = palette[0][aaa][2]
                    colourlab= cv2.cvtColor(colournp.astype(np.float32)/256, cv2.COLOR_RGB2Lab)[0][
                        0]
                    palettelab[0][aaa][0], palettelab[0][aaa][1], palettelab[0][aaa][2] = colourlab[0], colourlab[1], colourlab[2]
                    oneColouredPictures[aaa][:] = colourlab

                    oneColouredPictureDifferences[aaa] = colour.delta_E(imarray, oneColouredPictures[aaa])**2

                    if aaa == 0:
                        minimumarrayvalue = np.sum(oneColouredPictureDifferences[0])
                    else:
                        minimumarrayvalue = np.sum(
                            np.minimum(oneColouredPictureBestDifferences[aaa - 1], oneColouredPictureDifferences[aaa]))
                    if(minimumarrayvalue<bestvalue):
                        bestvalue = minimumarrayvalue
                        bestlab[0], bestlab[1], bestlab[2] = palettelab[0][aaa][0], palettelab[0][aaa][1], palettelab[0][aaa][2]
                        bestpalette[0],bestpalette[1],bestpalette[2] = palette[0][aaa][0],palette[0][aaa][1],palette[0][aaa][2]
                        #print(palette)
        print(bestpalette)
        paletteout[0][aaa][0], paletteout[0][aaa][1], paletteout[0][aaa][2] = bestlab[0], bestlab[1], bestlab[2]

        bestlab = np.ndarray((3,))
        bestvalue = 10000000000
        bestpalette2 = np.ndarray((3,))
        for r in range(48):
            palette[0][aaa][0] = bestpalette[0]-24+r
            if palette[0][aaa][0] < 0 or palette[0][aaa][0] >255:
                continue
            for g in range(48):
                #print(str(aaa) + " " + str(r) + " " + str(g) + " ")
                palette[0][aaa][1] = bestpalette[1]-24+g
                if palette[0][aaa][1] < 0 or palette[0][aaa][1] > 255:
                    continue
                for b in range(48):
                    palette[0][aaa][2] = bestpalette[2]-24+b
                    if palette[0][aaa][2] < 0 or palette[0][aaa][2] > 255:
                        continue

                    palettelab = paletteout.copy()
                    colournp = np.ndarray((1, 1, 3))
                    colournp[0][0][0] = palette[0][aaa][0]
                    colournp[0][0][1] = palette[0][aaa][1]
                    colournp[0][0][2] = palette[0][aaa][2]
                    colourlab = cv2.cvtColor(colournp.astype(np.float32) / 256, cv2.COLOR_RGB2Lab)[0][
                        0]
                    palettelab[0][aaa][0], palettelab[0][aaa][1], palettelab[0][aaa][2] = colourlab[0], colourlab[1], \
                    colourlab[2]
                    oneColouredPictures[aaa][:] = colourlab

                    oneColouredPictureDifferences[aaa] = colour.delta_E(imarray, oneColouredPictures[aaa]) ** 2

                    if aaa == 0:
                        minimumarrayvalue = np.sum(oneColouredPictureDifferences[0])
                    else:
                        minimumarrayvalue = np.sum(np.minimum(oneColouredPictureBestDifferences[aaa-1],oneColouredPictureDifferences[aaa]))
                    if (minimumarrayvalue < bestvalue):
                        bestvalue = minimumarrayvalue
                        bestlab[0], bestlab[1], bestlab[2] = palettelab[0][aaa][0], palettelab[0][aaa][1], \
                        palettelab[0][aaa][2]
                        bestpalette2[0], bestpalette2[1], bestpalette2[2] = palette[0][aaa][0], palette[0][aaa][1], \
                        palette[0][aaa][2]
        paletteout[0][aaa][0], paletteout[0][aaa][1], paletteout[0][aaa][2] = bestlab[0], bestlab[1], bestlab[2]
        oneColouredPictures[aaa][:] = bestlab
        oneColouredPictureDifferences[aaa] = colour.delta_E(imarray, oneColouredPictures[aaa]) ** 2
        print(bestpalette2)
        palette[0][aaa][0],palette[0][aaa][1],palette[0][aaa][2] = bestpalette2[0],bestpalette2[1],bestpalette2[2]
        for aab in range(max(0, aaa - numbercolours + 1), aaa+1):
            minimumarray = oneColouredPictureDifferences[max(0, aab - numbercolours + 1)]
            for i in range(max(0, aaa - numbercolours + 2), aab+1):
                minimumarray = np.minimum(minimumarray, oneColouredPictureDifferences[i])
            oneColouredPictureBestDifferences[aab] = minimumarray



    #print(paletteout)
    print(paletteout[:,numberIterations-numbercolours:])
    print(palette)

    return paletteout[:,numberIterations-numbercolours:]

def colorCodeWithPalette(picture, palettelab, outputname):
    imarray = cv2.cvtColor(cv2.imread(picture).astype(np.float32) / 255, cv2.COLOR_BGR2Lab)
    output = np.ndarray(imarray.shape)
    for x in range(len(imarray)):
        print(x)
        for y in range(len(imarray[x])):
            closestColour = 0
            closestDif = colour.delta_E([imarray[x][y]], [palettelab[0][0]])
            for i in range(1, palettelab.shape[1]):
                dif = colour.delta_E([imarray[x][y]], [palettelab[0][i]])
                if (dif < closestDif[0]):
                    closestDif = dif
                    closestColour = i
            output[x][y][0],output[x][y][1],output[x][y][2]= palettelab[0][closestColour][0],palettelab[0][closestColour][1],palettelab[0][closestColour][2]
    cv2.imwrite(outputname, (cv2.cvtColor((output.astype(np.float32)), cv2.COLOR_Lab2BGR).astype(np.float32) * 256).astype(np.uint8))
    print((cv2.cvtColor((output.astype(np.float32)),cv2.COLOR_Lab2BGR).astype(np.float32)*256).astype(np.uint8))


#palette = "c2c1a5,d3b57d,a1b1b3,b1976e,9a9288,808796,847774,657193,866a53,706b78,735b52,5b5a75,69585f,47548a,51465f,33356b,20202"

if __name__ == '__main__':
    #inputname = sys.argv[1]
    #outputname = sys.argv[2]
    #colorCodeWithPalette(inputname, findEfficient(51, inputname,17), outputname)
    imagename = "Mercury128x128.png"
    imageoutputname = "Mercury128x12817col.png"
    palette = GetHexCodesFromPicture.Get(imagename)
    bgrarray = sortPalette.stringToPaletteArrayBGR(palette)
    colournp = np.array(bgrarray,np.uint8).reshape((1,len(bgrarray),3))
    colourlab = cv2.cvtColor(colournp.astype(np.float32) / 256, cv2.COLOR_BGR2Lab)
    print(colourlab)
    colorCodeWithPalette(imagename,colourlab,imageoutputname)