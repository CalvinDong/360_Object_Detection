import random
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np
import yaml 
import os

random.seed(0)
class_id_to_name_mapping = {}
with open("/Users/calvindong/Documents/Repos/360_Object_Detection/generation/data.yml", "r") as stream:
    try:
        data = yaml.safe_load(stream)
        i = 0
        for fruit in data["names"]:
            class_id_to_name_mapping[i] = fruit
            i += 1
    except yaml.YAMLError as exc:
        print(exc)

print(class_id_to_name_mapping)

def plot_bounding_box(image, annotation_list):
    annotations = np.array(annotation_list)
    w, h = image.size
    
    plotted_image = ImageDraw.Draw(image)

    transformed_annotations = np.copy(annotations)
    transformed_annotations[:,[1,3]] = annotations[:,[1,3]] * w
    transformed_annotations[:,[2,4]] = annotations[:,[2,4]] * h 
    
    transformed_annotations[:,1] = transformed_annotations[:,1] - (transformed_annotations[:,3] / 2)
    transformed_annotations[:,2] = transformed_annotations[:,2] - (transformed_annotations[:,4] / 2)
    transformed_annotations[:,3] = transformed_annotations[:,1] + transformed_annotations[:,3]
    transformed_annotations[:,4] = transformed_annotations[:,2] + transformed_annotations[:,4]
    
    for ann in transformed_annotations:
        obj_cls, x0, y0, x1, y1 = ann
        plotted_image.rectangle(((x0,y0), (x1,y1)))
        
        plotted_image.text((x0, y0 - 10), class_id_to_name_mapping[(int(obj_cls))])
    
    plt.imshow(np.array(image))
    plt.show()

# Get any random annotation file 
#annotation_file = random.choice(annotations)
annotation_file = "/Users/calvindong/Documents/Repos/360_Object_Detection/generation/output/labels/1.txt"
with open(annotation_file, "r") as file:
    annotation_list = file.read().split("\n")[:-1]
    annotation_list = [x.split(" ") for x in annotation_list]
    annotation_list = [[float(y) for y in x ] for x in annotation_list]

#Get the corresponding image file
#image_file = annotation_file.replace("annotations", "images").replace("txt", "png")
image_file = "/Users/calvindong/Documents/Repos/360_Object_Detection/generation/output/images/1.jpg"
assert os.path.exists(image_file)

#Load the image
image = Image.open(image_file)

#Plot the Bounding Box
plot_bounding_box(image, annotation_list)