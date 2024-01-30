import os

from PIL import Image

if __name__ == '__main__':


   for imagename in os.listdir("BackgroundPlanetsTransparent"):
      print(imagename)
      image = Image.open("BackgroundPlanetsTransparent/" + imagename)
      resizedImage = image.resize((32,32))
      resizedImage.save("BackgroundPlanetsTransparent/32x32" + imagename, "PNG")
