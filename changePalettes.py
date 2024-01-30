import cv2
import numpy as np


def stringToPaletteArrayBGR(string):
    array = string.split(",")
    return [[int(s,16)%256, (int(s,16)//256)%256,(int(s,16)//256//256)%256] for s in array]


#palettein = "dbcac3,c0a597,a0959c,a0867b,88787c,6f6b7b,81685f,6c5d5f,55515f,544648,374364,3d3743,233050,1a2441,202231,0f1830" #image6 16col
palettein = "c2c1a5,d3b57d,a1b1b3,b1976e,9a9288,808796,847774,657193,866a53,706b78,735b52,5b5a75,69585f,47548a,51465f,33356b,20202" #Mercury128x12817col
#palettein = "e5ece7,d7dfe9,d5cec1,b9bebb,c6b8b0,b6aa9a,969a9a,a39586,ac8a81,8e8273,6e7170,796e5f,806a65,5f574b,47433d,2a2823,30303" # jupiternasa
#palettein = "e0c793,c2af85,a5a395,aa9c7a,91999d,97907a,88877f,7c8385,71818e,72736f,677074,596774,596063,4b4d4c,323537,1b1d1f,20202" # saturn
paletteout = "b3a199,9f887d,847e81,7d6b63,6f6b7b,81685f,6e6366,6c5d5f,55515f,544648,374364,3d3743,233050,1a2441,202231,f1830,000000,ffffff" #image6 16coldarker
paletteout = "ddffff,e0fcff,c8eeeb,c3ecea,a9dbef,fbc340,7dd8d2,f09421,64a6ca,ed6d1d,357db0,e65615,c73218,9f2d1a,901e20,712625,000000" #fireice
paletteout = "88eef2,94dc7b,6ce343,6abbbf,70ab59,479296,6874d3,558045,77614d,396e70,485cf5,3a582f,5a4736,384080,4c3623,23284d,000000,ffffff" #nature

if __name__ == '__main__':
    imarray = cv2.imread("Mercury128x12817col.png").astype(np.uint8)
    imarrayout = np.ndarray(imarray.shape)
    impal = stringToPaletteArrayBGR(palettein)
    outpal = stringToPaletteArrayBGR(paletteout)
    print(impal)
    for x in range(imarray.shape[0]):
        for y in range(imarray.shape[1]):
            imarrayout[x][y] = outpal[impal.index(imarray[x][y].tolist())]

    cv2.imwrite("Mercury128x128nature.png",imarrayout)