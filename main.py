from kivy.app import App
from kivy.uix.label import Label

class KivyMemoApp(App):
    def build(self):
        return Label(text="메모장 어플 입니다!")

if __name__ == "__main__":
    KivyMemoApp().run()