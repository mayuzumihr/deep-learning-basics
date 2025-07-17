import cv2
import numpy as np

# ResNet10ベースのSSDモデル（OpenCV Face Detector） 

# https://github.com/dkurt/cvpr2019/tree/master
# [opencv_face_detector.caffemodel](https://github.com/opencv/opencv_3rdparty/raw/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel)  
# [opencv_face_detector.prototxt](https://raw.githubusercontent.com/opencv/opencv/4.5.5/samples/dnn/face_detector/deploy.prototxt)  

'''

https://github.com/opencv/opencv/blob/4.9.0/samples/dnn/models.yml

opencv_fd:
  load_info:
    url: "https://github.com/opencv/opencv_3rdparty/raw/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel"
    sha1: "15aa726b4d46d9f023526d85537db81cbc8dd566"
  model: "opencv_face_detector.caffemodel"
  config: "opencv_face_detector.prototxt"
  mean: [104, 177, 123]
  scale: 1.0
  width: 300
  height: 300
  rgb: false
  sample: "object_detection"
'''

# capture = cv2.VideoCapture("./face.jpg")
capture = cv2.VideoCapture(0)       # Camera

if not capture.isOpened():
  raise IOError("Capture Error")

weights = "./model/opencv_face_detector.caffemodel"
config = "./model/opencv_face_detector.prototxt"

detection_model = cv2.dnn.DetectionModel(weights, config)
#detection_model.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
#detection_model.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

#scale = 1.0                   # スケールファクター
#size = (300, 300)             # 入力サイズ
#mean = (104.0, 177.0, 123.0)  # 差し引かれる平均値
#swap = False                  # チャンネルの順番（True: RGB、False: BGR）
#crop = False                  # クロップ
#detection_model.setInputParams(scale, size, mean, swap, crop)

while True:

  result, image = capture.read()

  if result is True: 

#    if len(image.shape) == 2:
#      channels = 1
#    else:
#      channels = image.shape[2]

#    if channels == 1:
#      image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
#    elif channels == 4:
#      image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

#    confidence_threshold = 0.6
#    nms_threshold = 0.4

#    classIds, confidences, boxes = detection_model.detect(image, confidence_threshold, nms_threshold)

    classIds, confidences, boxes = detection_model.detect(image)

    for box in boxes:
      color = (0, 255, 0)
      thickness = 2
      cv2.rectangle(image, box, color, thickness, cv2.LINE_AA)

    cv2.imshow("Face Detection", image)

  key = cv2.waitKey(10)

  if key == ord('q'):
    cv2.destroyAllWindows()
    break