import os
import random
import subprocess
import shutil

from tqdm import tqdm

def randomNumbers(fruitImages):
   randomSet = set()
   fruitTotal = len(fruitImages)
   proportion = int(fruitTotal * 0.35)
   while (len(randomSet) < proportion):
      randomSet.add(random.randint(0, fruitTotal) - 1)
   return randomSet

inputDir = "/Users/calvindong/Documents/Repos/Fruit-Images-Dataset/Training"
outputDir = "/Users/calvindong/Documents/Repos/360_Object_Detection/Datasets/AugmentFruits"

if (os.path.exists(outputDir) == False):
      newFruitClassDir = os.mkdir(outputDir)

fruits = os.listdir(inputDir)
for fruit in tqdm(fruits):
    if (fruit[0] == "."):
       continue
    
    fruitPath = os.path.join(inputDir, fruit)
    fruitImages = os.listdir(fruitPath)
    randomSet = randomNumbers(fruitImages)

    newFruitDir = os.path.join(outputDir, fruit)

    #Need to copy the original folder instead

    if (os.path.exists(newFruitDir) == False):
      shutil.copytree(fruitPath, newFruitDir)
  
    for num in randomSet:
      #print(fruitImages[num])
      if (num%2 == 1):
         cmd = f'convert "{os.path.join(fruitPath, fruitImages[num])}" -sample 100%x25% "{os.path.join(newFruitDir, fruitImages[num])}"'
      else:
         cmd = f'convert "{os.path.join(fruitPath, fruitImages[num])}" -virtual-pixel White -distort Arc 60  "{os.path.join(newFruitDir, fruitImages[num])}"'
      
      subprocess.call(cmd, shell=True)

        
    #print(proportion)

