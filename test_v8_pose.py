from ultralytics import YOLO
import cv2
# Load a model
model = YOLO('yolov8s-pose.pt')  # load an official model

cap = cv2.VideoCapture(0)   # 0表示默认摄像头，如果有多个摄像头，可以尝试使用1, 2, 等

# 遍历视频帧
while cap.isOpened():
    # 从视频中读取一帧
    success, frame = cap.read()

    if success:
        # 在该帧上运行YOLOv8推理
        results = model(frame)

        # 在帧上可视化结果
        annotated_frame = results[0].plot()

        # 显示带注释的帧
        cv2.imshow("YOLOv8_pose", annotated_frame)

        # 如果按下'q'则中断循环
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # 如果视频结束则中断循环
        break

# 释放视频捕获对象并关闭显示窗口
cap.release()
cv2.destroyAllWindows()

# 以下是其他例子
'''
# Predict with the model
results = model('https://ultralytics.com/images/bus.jpg')  # predict on an image

# Another way to predict with the model
#results = model.predict(img_array,save=True,save_txt=True,device='cpu',conf=0.65) 

# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    result.show()  # display to screen
    result.save(filename='result.jpg')  # save to disk
'''