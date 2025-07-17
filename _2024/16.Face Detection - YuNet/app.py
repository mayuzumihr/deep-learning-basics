import cv2

# capture = cv2.VideoCapture("./face.jpg")    # File
capture = cv2.VideoCapture(0)             # Camera

if not capture.isOpened():
  raise IOError("Capture Error")

width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

face_detector = cv2.FaceDetectorYN.create(  
  model="./model/face_detection_yunet_2023mar.onnx",
  config="",
  input_size=(width, height)
)

while True:

  result, image = capture.read()
  faces = face_detector.detect(image)

  if faces[1] is not None:
    for face in faces[1]:
      box = face[:4].astype(int)
      color = (0, 255, 0)
      thickness = 2
      cv2.rectangle(image, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]), color, thickness)

  cv2.imshow("Face Detection", image)

  key = cv2.waitKey(10)

  if key == ord('q'):
    cv2.destroyAllWindows()
    break





