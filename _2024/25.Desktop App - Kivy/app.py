from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.text import LabelBase
from kivy.core.window import Window

LabelBase.register(name='Meiryo', fn_regular='C:/Windows/Fonts/meiryo.ttc')

class GUISample(GridLayout):

  def __init__(self, **kwargs):

    super(GUISample, self).__init__(**kwargs)

    self.cols = 1
    self.padding = [20, 20, 20, 20]
    self.spacing = 20
    
    self.text = TextInput(font_name='Meiryo', size_hint_y=None, height=30)
    self.add_widget(self.text)
    
    self.label = Label(text='ここにテキストが表示されます', font_name='Meiryo', size_hint_y=None, height=30)
    self.add_widget(self.label)
    
    button_layout = BoxLayout(size_hint_y=None, height=30)
    button_layout.add_widget(BoxLayout())
    self.button = Button(text='ボタン', font_name='Meiryo', size_hint_x=None, width=100, height=30)
    self.button.bind(on_press=self.show_text)
    button_layout.add_widget(self.button)
    button_layout.add_widget(BoxLayout())
    
    self.add_widget(button_layout)
  
  def show_text(self, instance):
    input_text = self.text.text
    self.label.text = input_text

class MyApp(App):

  def build(self):
    self.title = 'サンプルアプリ（Kivy）'
    Window.size = (500, 300)
    return GUISample()

if __name__ == '__main__':
  MyApp().run()
