# Autonomous Driving using Computer Vision
PS: This contest aims to utilize the Cityscapes 3D dataset (paper | website) for the vision-based perception of a self-driving car's surroundings. This Cityscapes 3D dataset is an extension of the Original Cityscapes dataset with 3D bounding box annotations for all types of vehicles. It comprises images from the front camera, which helps in performing tasks like 2D & 3D bounding box detections, semantic segmentations, etc. There can be multiple individual models for each task. However, in this hackathon, your task is to train a Multitask or Multinet perception model to simultaneously perform object detection (through 3D bounding box detection) and driving path recognition (through semantic segmentation) on this Cityscapes dataset to achieve top accuracy levels for real-world use cases. 

Our Approach: To perform real-time object detection, we will use two approaches:

1. Single Shot Detection(SSD)

2. YOLO (You Only Look Once)

We will compare the above two models in terms of:

1. Good Accuracy/Loss Function

2. Low Inference Time
