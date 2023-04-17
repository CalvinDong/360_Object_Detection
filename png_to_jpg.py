from PIL import Image
import cv2
import os

#for file in os.listdir("E:\Backgrounds"):
path = os.path.join("E:\Backgrounds")
for file in os.listdir(path):
  if file.endswith(".png"):
    print(file)
    name = os.path.splitext(file)[0]
    newName = name + '.jpg'
    filePath = os.path.join(path, file)
    newPath =  f"{path}\{name}.jpg"
    #img_png = Image.open(filePath)
    #img_png.save(newPath)
    png_img = cv2.imread(filePath)
    cv2.imwrite(newPath, png_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
    os.remove(filePath)
    