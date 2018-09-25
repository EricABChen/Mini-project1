# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 15:00:30 2018

@author: 18004
"""

import io
import os
from google.cloud import vision
from google.cloud.vision import types

# install a client
client = vision.ImageAnnotatorClient()

# load the image file    
os.listdir(r'users/18004/desktop/ec601/project1/image')
os.chdir(r'users/18004/desktop/ec601/project1/image')

for image in os.listdir():
    if image.endswith(".jpg"):
        file_name = os.path.join(os.path.dirname(__file__), image)

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()


# detect labels of the images using google API
    image = vision.types.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    
# print out the name of each picture
    print('Labels:')
    label_list = []
    for item in labels:
        label_list.append(item.description)
        print(item.description)
    
    print(label_list)

