import json
import os

DATASET_PATH = '.'
def load_captions(set = 'val'):
    annotation_file_name = 'captions_' + set + '2017.json'
    annotation_file_path = os.path.join(DATASET_PATH, annotation_file_name)
    
    with open(annotation_file_path) as f:
        return json.load(f)
    
def get_image_path(image_file_name, set = 'val'):
    return os.path.join(DATASET_PATH, set + '2017', image_file_name)

def get_image_info_dict():
    set = 'val'
    image_info_dict = {}
    annotations_obj = load_captions(set)
    
    for images_obj in  annotations_obj['images']:
        image_info_dict[images_obj['id']] = {
            'file_path' : get_image_path(images_obj['file_name']),
            'file_name' : images_obj['file_name']
        }
    
    for ann_obj in annotations_obj['annotations']:
        image_info_dict[ann_obj['image_id']]['caption'] = ann_obj['caption']
    
    return image_info_dict

image_info_dict = get_image_info_dict()

print(len([image_info_dict[id]['caption'] for id in image_info_dict.keys()]))