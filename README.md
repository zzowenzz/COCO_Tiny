# Tiny MSCOCO2017 Dataset
Welcome to the Tiny COCO Dataset repository! This project aims to provide a simplified and fast-to-use version of the extensive COCO dataset for quick debugging and development of image processing models. The base version of this dataset contains exactly **one image per category**, making it lightweight and perfect for testing algorithms quickly.

# About COCO
The [COCO](https://cocodataset.org/#download) (Common Objects in Context) dataset is a large-scale object detection, segmentation, and captioning dataset. COCO is widely used in the machine learning community for benchmarking state-of-the-art models.

# About Tiny COCO
The Tiny COCO Dataset is a subset of the full COCO dataset and has been structured to provide immediate access to a smaller, more manageable collection of images across all categories. This is ideal for:
- **Rapid Prototyping**: Quickly test and debug models without the overhead of working with tens of gigabytes of data.
- **Educational Purposes**: Learn model building with a real-world dataset without significant hardware limitations.

# Base Version
The base version of this dataset includes:

- **1 image per category** for both training (train) and validation (val) sets.
- Annotations in COCO format that correspond to these images.

# Data Customization
Users are encouraged to generate customized versions of the dataset with more images per category, depending on specific requirements. The repository includes Python scripts to facilitate this process.

# Usage
## Clone this repository
```
git clone https://github.com/zzowenzz/COCO_Tiny.git
cd COCO_Tiny
```

## Set up the environment
```
pip install -r requirements.txt
```


# Run the scripts
```
python make_dataset.py \\
    --coco_path [path to the original MSCOCO2017 dataset] \\
    --mini_path data/COCO_Tiny [path to save the Tiny COCO dataset] \\
    --num_img [number of images per category] 
```

# Contributions
Contributions to this project are welcome! Please consider the following ways to contribute:

- **Improvements**: Suggestions for improving the dataset or scripts.
- **Bug Reports**: Identify and report issues in the dataset generation script.
- **Documentation**: Enhancements to the README or additional guidelines.

# License
No license for this dataset. Feel free to use it for any purpose. For more, please refer to the [Terms of Use of the COCO dataset](https://cocodataset.org/#termsofuse).