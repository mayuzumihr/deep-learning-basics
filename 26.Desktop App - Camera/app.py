import cv2
import tkinter as tk
from tkinter import Button
from PIL import Image, ImageTk

class CameraApp:
  def __init__(self, window, window_title):
    self.window = window
    self.window.title(window_title)
    self.window.geometry('800x600')

    self.video_source = 0
    self.vid = cv2.VideoCapture(self.video_source)
    
    self.canvas = tk.Canvas(window, width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    self.canvas.pack()
    
    self.btn_snapshot = Button(window, text="キャプチャー", width=30, command=self.snapshot)
    self.btn_snapshot.pack(anchor=tk.CENTER, expand=True)
    
    self.update()
    self.window.mainloop()
    
  def snapshot(self):
    ret, frame = self.vid.read()
    if ret:
      cv2.imwrite("captured_image.jpg", cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
      print("画像を保存しました")
      
  def update(self):
    ret, frame = self.vid.read()
    if ret:
      self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
      self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
      
    self.window.after(10, self.update)
    
  def __del__(self):
    if self.vid.isOpened():
      self.vid.release()
      
if __name__ == "__main__":
  root = tk.Tk()
  app = CameraApp(root, "カメラビューアー（Tkinter）")