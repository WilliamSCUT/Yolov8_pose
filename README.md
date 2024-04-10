# Yolov8_pose

This project mainly includes the implementation of a pose estimation based on the yolov8-pose model.

### Repo Structure
- ``test_v8_pose.py`` Load the trained model for testing.

### Installation

    conda create -n yolo python=3.8
    conda activate yolo
    pip install ultralytics

### Example Usages

To set up a new terminal, run:

    conda activate yolo
    cd <path to act repo>

### Pose Model Training
To train the pose model Start training from a pretrained *.pt model, run:


    yolo pose train data=coco8-pose.yaml model=yolov8s-pose.pt epochs=100 imgsz=640


You can dynamically adjust parameters such as epochs according to the size and complexity of the data set, or modify the data path to your own data path.


### Model Testing
To test the model with our usb camera, run:

    test_v8_pose.py
