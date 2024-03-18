
# Explanation of Yolo format Readme.md

Yolo is more a folder format that a text output format: 

Yolov5 data set file would look like this:

dataset.yaml 
```
path: /data/  
train: train/images
val: val/images

nc: 2

names:
  - background
  - detection
```  

A Proper dataset would look like this:
Tree structure of folders and dataset.yaml 
```
.
├── dataset.yaml
├── train
│   ├── images
│   │   ├── 0.png
│   │   └── 1.png
│   └── labels
│       ├── 0.txt
│       └── 1.txt
└── val
    ├── images
    │   ├── 0.png
    │   └── 1.png
    └── labels
        ├── 0.txt
        └── 1.txt
```

labels have the format below 
each line looks like the below: 

```
1 0.44765625000000003 0.7976562500000001 0.0421875 0.035937500000000004
```

Breaking down each section, which are separated by spaces. 
`<object-class> <x-center> <y-center> <width> <height>`

1 - this is the label number from the dataset.yaml file for the object-classes sepcified in the names section of the dataset.yaml 
Measure from the top left corner in proportion to the size of the image. 

