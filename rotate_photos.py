import os
import argparse

import piexif
import PIL
from PIL import Image, ExifTags
from tqdm import tqdm


def rotate(folder_path):
  print("Rotate the files here")
  files = os.listdir(folder_path)
  Image.MAX_IMAGE_PIXELS = None # Prevent PIL max image size protection failure (thinks a compression attack is occurring)
  for file in tqdm(files):
    try:
      image_path = os.path.join(folder_path, file)
      image = Image.open(image_path)
      exif_dict = piexif.load(image.info["exif"])

      if exif_dict['0th'][piexif.ImageIFD.Orientation] != 1: # Check if orientation is right way up in image exif
        print(file)
        exif_dict['0th'][piexif.ImageIFD.Orientation] = 1
        exif_bytes = piexif.dump(exif_dict)
        image.save(image_path, "jpeg", exif=exif_bytes)

      if image.height > image.width:    
        image = image.rotate(90, PIL.Image.NEAREST, expand = 1)
        image.save(image_path)
      else:
        continue
    except Exception as e:
      print(e)


if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    prog='Rotate_Photos',
    description='Trying to rotate any photos that are currently in a portrait aspect ratio',
  )

  parser.add_argument(dest='folder_path', metavar='p',
    help="the path to the folder containing the images you want to go through"
  )

  args = parser.parse_args()
  rotate(args.folder_path)

  # HOW TO USE
  # Run the python file with the first parameter as the path to the folder containing the images
  # Example  python filter_photos.py /Users/calvindong/Documents/Repos/flickr-scrape/images/group_91922148_N00