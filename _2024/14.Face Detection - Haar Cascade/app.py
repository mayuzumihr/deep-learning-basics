
import cv2
import numpy as np

# capture = cv2.VideoCapture("./face.jpg")
capture = cv2.VideoCapture(0)        # Camera

if not capture.isOpened():
  raise IOError("Capture Error")

cascade = cv2.CascadeClassifier("./model/haarcascade_frontalface_default.xml")

while True:

  result, image = capture.read()

  if result is True:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = gray_image.shape
    min_size = (int(width / 10), int(height / 10))
    boxes = cascade.detectMultiScale(gray_image, minSize=min_size)

    for box in boxes:
      color = (0, 255, 0)
      thickness = 2
      cv2.rectangle(image, box, color, thickness, cv2.LINE_AA)

    cv2.imshow("Face Detection", image)

  key = cv2.waitKey(10)

  if key == ord('q'):
    cv2.destroyAllWindows()
    break     

'''
ファイル名	内容
haarcascade_eye.xml	目
haarcascade_eye_tree_eyeglasses.xml	眼鏡
haarcascade_frontalcatface.xml	猫の顔（正面）
haarcascade_frontalcatface_extended.xml	猫の顔（正面）
haarcascade_frontalface_alt.xml	顔（正面）
haarcascade_frontalface_alt2.xml	顔（正面）
haarcascade_frontalface_alt_tree.xml	顔（正面）
haarcascade_frontalface_default.xml	顔（正面）
haarcascade_fullbody.xml	全身
haarcascade_lefteye_2splits.xml	左目
haarcascade_licence_plate_rus_16stages.xml	ロシアのナンバープレート（全体）
haarcascade_lowerbody.xml	下半身
haarcascade_profileface.xml	顔（証明写真）
haarcascade_righteye_2splits.xml	右目
haarcascade_russian_plate_number.xml	ロシアのナンバープレート（数字）
haarcascade_smile.xml	笑顔
haarcascade_upperbody.xml	上半身
'''