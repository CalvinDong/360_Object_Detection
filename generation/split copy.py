import os
import random
import shutil

def getTrain(images):
   randomSet = set()
   total = len(images)
   proportion = int(total * 0.7) # How much we want to split into the training set
   print(proportion)
   while (len(randomSet) < proportion):
      randomSet.add(random.randint(0, total) - 1)
   return randomSet

folderPath = "/Users/calvindong/Documents/Repos/360_Object_Detection/Datasets/PanoramicFruitsReal_Base2"
imagePath = os.path.join(folderPath, "images")
labelPath = os.path.join(folderPath, "labels")
targetPath = "/Users/calvindong/Documents/Repos/360_Object_Detection/Datasets/PanoramicFruitsRealVal"

if (os.path.exists(targetPath) == False):
  os.mkdir(targetPath)
  os.mkdir(os.path.join(targetPath, "test"))
  os.mkdir(os.path.join(targetPath, "test_labels"))
  #os.mkdir(os.path.join(targetPath, "test"))

images = os.listdir(imagePath)
images.sort()
print(images)
labels = os.listdir(labelPath)
labels.sort()
print(labels)
trainImages = getTrain(images)

shutil.copytree(imagePath, os.path.join(targetPath, "val"))
shutil.copytree(labelPath, os.path.join(targetPath, "val_labels"))

for num in trainImages:
  shutil.move(os.path.join(os.path.join(targetPath, "val"), images[num]), os.path.join(targetPath, "test"))
  shutil.move(os.path.join(os.path.join(targetPath, "val_labels"), labels[num]), os.path.join(targetPath, "test_labels"))
