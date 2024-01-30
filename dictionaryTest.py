import numpy as np

dic = {}
if dic.get((0,1)) is None:
    dic.update({(0,1): np.full((1),0)})
    print("updated")
print(dic)