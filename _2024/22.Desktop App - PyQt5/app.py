import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton

class GUISample(QWidget):

  def __init__(self):
    super().__init__()
    self.setWindowTitle('サンプルアプリ（PyQt5）')
    self.setGeometry(100, 100, 500, 300)
    
    layout = QVBoxLayout()
    
    self.text = QLineEdit(self)
    self.text.setFixedHeight(30)
    layout.addWidget(self.text)
    
    label_layout = QHBoxLayout()
    self.label = QLabel('ここにテキストが表示されます', self)
    label_layout.addStretch(1)
    label_layout.addWidget(self.label)
    label_layout.addStretch(1)
    layout.addLayout(label_layout)
    
    button_layout = QHBoxLayout()
    self.button = QPushButton('ボタン', self)
    button_layout.addStretch(1)
    button_layout.addWidget(self.button)
    button_layout.addStretch(1)
    layout.addLayout(button_layout)
    
    self.button.clicked.connect(self.show_text)
    self.setLayout(layout)
  
  def show_text(self):
    input_text = self.text.text()
    self.label.setText(input_text)

def main():
  app = QApplication(sys.argv)
  sample = GUISample()
  sample.show()
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()