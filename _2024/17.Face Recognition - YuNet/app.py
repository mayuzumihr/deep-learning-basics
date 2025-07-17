import cv2

#===================================================================#
# モデルのロード（顔検出）
#===================================================================#
capture = cv2.VideoCapture(0)            # Camera

if not capture.isOpened():
  raise IOError("Capture Error")

width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

face_detector = cv2.FaceDetectorYN.create(  
  model="./model/face_detection_yunet_2023mar.onnx",
  config="",
  input_size=(width, height)
)

#===================================================================#
# モデルのロード（顔認識）
#===================================================================#
face_recognizer = cv2.FaceRecognizerSF.create(  
  model="./model/face_recognition_sface_2021dec.onnx",
  config=""
)

picture_path = ["./abiko.jpg", "./mayuzumi.jpg", "./sueyoshi.jpg", "./iwahori.jpg", "./lautan.jpg", "./lawrence.jpg"]
picture_label = ["abiko", "mayuzumi", "sueyoshi", "iwahori", "lautan", "lawrence"]
picture_feature = []

for i in range(len(picture_path)):

  picture = cv2.imread(picture_path[i])
  picture = cv2.resize(picture, (width, height))
  faces = face_detector.detect(picture)

  if faces[1] is not None:
    picture_aligned = face_recognizer.alignCrop(picture, faces[1][0])
    picture_feature.append(face_recognizer.feature(picture_aligned))

#===================================================================#
# カメラから映像を取得
#===================================================================#
while True:

  result, image = capture.read()
  faces = face_detector.detect(image)

  if faces[1] is not None:

    for face in faces[1]:

      image_aligned = face_recognizer.alignCrop(image, face)
      image_feature = face_recognizer.feature(image_aligned)
      score = []

      for picture_feature_element in picture_feature:
        score.append(face_recognizer.match(image_feature, picture_feature_element, cv2.FaceRecognizerSF_FR_COSINE))

      max_value_index = score.index(max(score))

      box = face[:4].astype(int)
      color = (0, 255, 0)
      size = 1
      thickness = 2

      cv2.rectangle(image, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]), color, thickness)
      cv2.putText(image, picture_label[max_value_index], (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, size, color, thickness)

  cv2.imshow("Face Detection", image)

  key = cv2.waitKey(10)

  if key == ord('q'):
    cv2.destroyAllWindows()
    break