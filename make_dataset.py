import os
import shutil
import json
from pycocotools.coco import COCO
import argparse

def setup_mini_coco(coco_path, mini_path, data_types, num_img):
    """
    Create a mini COCO dataset with a specified number of images per category
    Args:
        coco_path: Path to the COCO dataset
        mini_path: Path to store the mini dataset
        data_types: List of data types to create mini dataset for (e.g., ['train', 'val'])
        num_img: Number of images per category
    """
    images_used = set()  # Set to track used images to ensure no duplication across types

    for data_type in data_types:
        ann_file = os.path.join(coco_path, 'annotations', f'instances_{data_type}2017.json')
        coco = COCO(ann_file)
        
        # Directory for mini dataset
        mini_dir = os.path.join(mini_path, f'{data_type}2017')
        os.makedirs(mini_dir, exist_ok=True)
        
        # Prepare the structure of the new JSON file
        new_ann_file = {
            "images": [],
            "annotations": [],
            "categories": coco.loadCats(coco.getCatIds())
        }

        # Get all categories and select specified number of images per category
        categories = coco.loadCats(coco.getCatIds())
        cat_ids = [cat['id'] for cat in categories]
        img_counter = 1  # To create new image ids
        
        for cat_id in cat_ids:
            img_ids = coco.getImgIds(catIds=[cat_id])
            selected_imgs = [img_id for img_id in img_ids if img_id not in images_used][:num_img]

            for selected_img in selected_imgs:
                images_used.add(selected_img)
                img_info = coco.loadImgs(selected_img)[0]
                img_info['id'] = img_counter
                new_ann_file['images'].append(img_info)
                
                # Copy image to mini dataset directory
                shutil.copy(os.path.join(coco_path, f'{data_type}2017', img_info['file_name']),
                            os.path.join(mini_dir, img_info['file_name']))
                
                # Get all annotations for the selected image and modify them
                ann_ids = coco.getAnnIds(imgIds=[selected_img])
                annotations = coco.loadAnns(ann_ids)
                for ann in annotations:
                    ann['image_id'] = img_counter
                    new_ann_file['annotations'].append(ann)
                
                img_counter += 1  # Increment the counter for new image IDs

        # Save the new JSON file
        ann_output_dir = os.path.join(mini_path, 'annotations')
        os.makedirs(ann_output_dir, exist_ok=True)
        with open(os.path.join(ann_output_dir, f'instances_{data_type}2017.json'), 'w') as f:
            json.dump(new_ann_file, f, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create a mini COCO dataset")
    parser.add_argument('--coco_path', type=str, required=True,
                        help='Directory where COCO dataset is stored')
    parser.add_argument("--mini_path", type=str, required=True, help="Directory to store mini dataset")
    parser.add_argument("--num_img", type=int, default=1,
                        help="Number of images per category")

    args = parser.parse_args()
    setup_mini_coco(args.coco_path, args.mini_path, ['train', 'val'], args.num_img)
