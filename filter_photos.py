import os
import argparse
import shutil
from PIL import Image
from tqdm import tqdm

def filter(folder_path):
  print("filter the files here")
  if not os.path.isdir("data"):
    os.mkdir(os.path.join(folder_path, "discarded"))
  
  files = os.listdir(folder_path)
  for file in tqdm(files):
    image_path = os.path.join(folder_path, file)
    #print(image_path)
    try:
      image = Image.open(image_path)
      Image.MAX_IMAGE_PIXELS = None # Prevent PIL max image size protection failure (thinks a compression attack is occurring)

      if image.height/image.width > 0.6: # Try to remove any little big planet photos which tend to have a a more 1:1 ratio or 0.7
        shutil.move(image_path, os.path.join(folder_path, "discarded" ,file))
    except Exception as e:
      print(e)
  
  print("Done!")



if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    prog='Filter_Photos',
    description='Trying to seperate little planet photos from quirectiangular 360 photos',
  )

  parser.add_argument(dest='folder_path', metavar='p',
    help="the path to the folder containing the images you want to sort"
  )

  args = parser.parse_args()
  filter(args.folder_path)

  # HOW TO USE
  # Run the python file with the first parameter as the path to the folder containing the images
  # Example  python filter_photos.py /Users/calvindong/Documents/Repos/flickr-scrape/images/group_91922148_N00




