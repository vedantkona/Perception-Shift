#!/usr/bin/env python
# coding: utf-8

# In[3]:


import torch
import numpy as np
import pandas as pd
from pycocotools.coco import COCO
import json
import csv


# In[4]:


with open('annotations/instances_train2017.json', 'r') as f:
    dataset = json.load(f)
    
coco = COCO('annotations/instances_train2017.json')


# In[5]:


categories = {}
for category in dataset['categories']:
    categories[category['id']] = category['name']


# In[6]:


object_labels = {}
max_labels = 0
for annotation in dataset['annotations']:
    image_id = annotation['image_id']
    category_id = annotation['category_id']
    label = categories[category_id]
    
    if image_id not in object_labels:
        object_labels[image_id] = [label]
    else:
        object_labels[image_id].append(label)
    
    num_labels = len(object_labels[image_id])
    if num_labels > max_labels:
        max_labels = num_labels

# Generate fieldnames for CSV writer
fieldnames = ['Image_Number'] + [f'Label{i+1}' for i in range(max_labels)]
    
with open('Object_Labels.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for image_id in object_labels:
        row = {'Image_Number': image_id}
        for i, label in enumerate(object_labels[image_id]):
            row[f'Label{i+1}'] = label
        writer.writerow(row)


# In[7]:


object_labels_df = pd.read_csv('Object_Labels.csv', low_memory=False)
object_labels_df.head(5)


# In[8]:


cat_ids = coco.getCatIds(catNms=['person'])
assert len(cat_ids) == 1
person_cat_id = cat_ids[0]


# In[9]:


human_pixels = {}
maxi_lables = 0
for annotation in dataset['annotations']:
    image_id = annotation['image_id']
    bbox_area = annotation['bbox'][2] * annotation['bbox'][3]
    category_id = annotation['category_id']
    label = categories[category_id]
    if annotation['category_id'] != person_cat_id:
        continue
    
    if image_id not in human_pixels:
        human_pixels[image_id] = [bbox_area]
    else:
        human_pixels[image_id] += [bbox_area]
    
    num_labels = len(object_labels[image_id])
    if num_labels > max_labels:
        max_labels = num_labels

# Generate fieldnames for CSV writer
fieldnames = ['Image_Number'] + [f'Human{i+1}' for i in range(max_labels)]

with open('Human_Pix.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for image_id, pixels in human_pixels.items():
        row = {'Image_Number': image_id}
        for i, label in enumerate(pixels):
            row[f'Human{i+1}'] = f'{label:.2f}'
        writer.writerow(row)


# In[10]:


human_pixels_df = pd.read_csv('Human_Pix.csv')
human_pixels_df = human_pixels_df.fillna(0)
human_pixels_df.to_csv('Human_Pixels.csv', index=False)
human_pixels_df


# In[11]:


human_volumes = {}
human_auras = {}
max_labels = 0

for annotation in dataset['annotations']:
    image_id = annotation['image_id']
    bbox_width = annotation['bbox'][2]
    bbox_height = annotation['bbox'][3]
    bbox_surface_area = bbox_width * bbox_height 
    category_id = annotation['category_id']
    label = categories[category_id]
    
    # Skip annotations that are not humans
    if label != 'person':
        continue
    
    # Calculate human volume and aura
    volume = bbox_surface_area * annotation['bbox'][2]
    if bbox_surface_area > 0:
        aura = volume / bbox_surface_area
    else:
        aura = 0
    
    if image_id not in human_volumes:
        human_volumes[image_id] = [volume]
        human_auras[image_id] = [aura]
    else:
        human_volumes[image_id] += [volume]
        human_auras[image_id] += [aura]
    
    num_labels = len(human_volumes[image_id])
    if num_labels > max_labels:
        max_labels = num_labels


# In[12]:


fieldnames = ['Image_Number'] + [f'Human{i+1}' for i in range(max_labels)]

# Write CSV file for human volumes
with open('Human_Vol.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for image_id, volumes in human_volumes.items():
        row = {'Image_Number': image_id}
        for i, volume in enumerate(volumes):
            row[f'Human{i+1}'] = f'{volume:.2f}'
        writer.writerow(row)
        
Human_Volumes_df = pd.read_csv('Human_Vol.csv')
Human_Volumes_df = Human_Volumes_df.fillna(0)
Human_Volumes_df.to_csv('Human_Volumes.csv', index=False)

        
# Write CSV file for human auras
fieldnames = ['Image_Number'] + [f'Human{i+1}' for i in range(max_labels)] + ['Aura']
with open('HumanAuras.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for image_id, auras in human_auras.items():
        row = {'Image_Number': image_id}
        for i, aura in enumerate(auras):
            row[f'Human{i+1}'] = f'{aura:.2f}'
        row['Aura'] = f'{sum(auras) / len(auras):.2f}'
        writer.writerow(row)
        
Human_Auras_df = pd.read_csv('HumanAuras.csv')
Human_Auras_df = Human_Auras_df.fillna(0)
Human_Auras_df.to_csv('Human_Auras.csv', index=False)

Human_Auras_df


# In[14]:


with open('Human_Auras.csv', 'r') as f:
    reader = csv.DictReader(f)
    auras = []
    for row in reader:
        auras += [float(row['Aura'])]
        
aurass = sum(auras)
aurass = round(aurass, 2)
print(aurass)
average_aura = aurass / len(auras)

with open('Average_Aura.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Average Aura'])
    writer.writerow([f'{average_aura:.2f}'])


# In[15]:


Aura_ddf = pd.read_csv('Average_Aura.csv')
Aura_ddf


# In[ ]:




