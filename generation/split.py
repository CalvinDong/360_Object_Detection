import os
import random
import shutil
import time

def getTrain(images):
   randomSet = set()
   total = len(images)
   proportion = int(total * 0.7) # How much we want to split into the training set
   print(proportion)
   while (len(randomSet) < proportion):
      randomSet.add(random.randint(0, total) - 1)
   return randomSet

folderPath = "/Users/calvindong/Documents/Repos/360_Object_Detection/Datasets/PanoramicFruitsReal_Base"
imagePath = os.path.join(folderPath, "images")
labelPath = os.path.join(folderPath, "labels")
targetPath = "/Users/calvindong/Documents/Repos/360_Object_Detection/Datasets/PanoramicFruitsReal"

if (os.path.exists(targetPath) == False):
  os.mkdir(targetPath)
  #os.mkdir(os.path.join(targetPath, "train"))
  #os.mkdir(os.path.join(targetPath, "train_labels"))
  #os.mkdir(os.path.join(targetPath, "test"))

images = os.listdir(imagePath)
images.sort()
#print(images)
labels = os.listdir(labelPath)
labels.sort()
#print(labels)
trainImages = getTrain(images)
print(trainImages)

shutil.copytree(imagePath, os.path.join(targetPath, "test"))
shutil.copytree(labelPath, os.path.join(targetPath, "test_labels"))

time.sleep(10)

for num in trainImages:
  shutil.move(os.path.join(os.path.join(targetPath, "test"), images[num]), os.path.join(targetPath, "train"))
  shutil.move(os.path.join(os.path.join(targetPath, "test_labels"), labels[num]), os.path.join(targetPath, "train_labels"))
