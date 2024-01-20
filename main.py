import os

import PIL
from PIL import Image, ImageEnhance


palrgbold = [0xdadce7, 0xb5b9cf,0x9096b6, 0x777ea6, 0x616894

   ]

palmeteroid = [0xdadce7, 0x9096b6, 0x616894, 0x404463, 0x282b3e, 0x181a25, 0x08090c, 0xeee6c8, 0x7a6b53, 0x4a3625, 0x302a24

   ]
palmysticstring = "FFE3BB,FFDBBB,FFD6BD,FFD5C4,FECDBF,FFC8C3,FFC3C2,FFBFC3,FFBAC4,FFB7C5,F5B8C1,F3AEC3,F3A6C6,F7A1C8,EF97C7,DD8CC6,D488C6,CB85C3,A776BB,976FB6,8569B4,7762B1,715BA4"

palmystic = [int(a,16) for a in palmysticstring.split(",")]
def rgbtoarray(rgb):
   return [(rgb >> 16) % 256, (rgb >> 8) % 256, rgb % 256]

def paletter(image, palette):
   pal2d = [rgbtoarray(rgb) for rgb in palette]
   pal = [item for sub_list in pal2d for item in sub_list]
   p_img = Image.new('P', (16, 32))
   p_img.putpalette(pal)

   im1 = image
   im2 = im1.resize((32, 32), Image.LANCZOS)
   im3 = ImageEnhance.Brightness(im2).enhance(1)

   new = im3.quantize(palette=p_img, dither=0)
   return new


if __name__ == '__main__':

   IMAGENAME = "image5.jpg"
   PALETTE = palmeteroid
   WIDTHCOUNT = 8
   HEIGHTCOUNT = 8

   os.mkdir("MainOutput")
   image = Image.open(IMAGENAME)
   for x in range(WIDTHCOUNT):
      for y in range(HEIGHTCOUNT):
         im1 = image.crop((x*image.width/WIDTHCOUNT, y*image.height/HEIGHTCOUNT, (x+1)*image.width/WIDTHCOUNT, (y+1)*image.height/HEIGHTCOUNT))
         paletter(im1, PALETTE).save("MainOutput/" + str(x) + "_" + str(y) + ".png", "PNG")




