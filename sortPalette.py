

def arrayBGRToString(array):
    palettedec = [hex(int(a[2] * 256 * 256 + a[1] * 256 + a[0])) for a in array]
    string = ""
    for a in palettedec:
        string+=a.split("x")[1]
        string+=","
    return string

def stringToPaletteArrayBGR(string):
    array = string.split(",")
    return [[int(s,16)%256, (int(s,16)//256)%256,(int(s,16)//256//256)%256] for s in array]

inputstring = "3a582f,94dc7b,6ce343,88eef2,6abbbf,479296,396e70,23284d,384080,6874d3,485cf5,4c3623,5a4736,77614d,558045,70ab59,000000"

if __name__ == '__main__':
    newlistsorted = sorted(stringToPaletteArrayBGR(inputstring),
                           key=lambda color: -(color[0] * 0.0722 + color[1] * 0.7152 + color[2] * 0.2126))
    print(arrayBGRToString(newlistsorted))

