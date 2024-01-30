import numpy as np


palette = [[ 111. , 111. , 127.],
  [ 175. , 159.  ,159.],
  [  47. ,  63. ,  95.],
  [ 127. , 111. , 111.],
  [ 223. , 191. , 175.],
  [  63. ,  79.,  111.],
  [  47. ,  47. ,  63.],
  [  79. ,  79.  , 95.]]


if __name__ == '__main__':
    palettedec = [hex(int(a[0]*256*256+a[1]*256+a[2]))  for a in palette]
    for a in palettedec:
        print(a.split("x")[1],end=",")