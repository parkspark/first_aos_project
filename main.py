from kivy.app import App
from kivy.uix.label import Label
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

resource_add_path('.')
LabelBase.register(DEFAULT_FONT, "./MaruBuriTTF/MaruBuri-Regular.ttf")

class KivyMemoApp(App):
    def build(self):
        return Label(text="메모장 어플 입니다!")

if __name__ == "__main__":
    KivyMemoApp().run()