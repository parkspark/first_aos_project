from kivy.app import App
from kivy.uix.label import Label
from kivy.core.text import LabelBase, DEFAULT_FONT # font
from kivy.resources import resource_add_path # font
from kivy.uix.boxlayout import BoxLayout # ui
from kivy.uix.textinput import TextInput # ui
from kivy.uix.button import Button # ui

resource_add_path('.')
LabelBase.register(DEFAULT_FONT, "./MaruBuriTTF/MaruBuri-Regular.ttf")

# class KivyMemoApp(App):
#     def build(self):
#         return Label(text="메모장 어플 입니다!")

class MemoLayout(BoxLayout): # BoxLayout을 상속받아 앱의 레이아웃 정의
    def __init__(self, **kwargs):
        super(MemoLayout, self).__init__(**kwargs)
        self.orientation = "vertical" #orientation 속성을 vertical로 설정 : 위에서 아래로 위젯 배치

        self.memo_input = TextInput( # TextInput 위젯 : 메모 작성 텍스트 입력 상자 
            hint_text="메모를 입력하세요...", # hint_text : 안내 문구
            multiline=True # multiline 을 True 로 여러줄 텍스트 입력 가능
            ) 
        self.add_widget(self.memo_input) # memo_input 위젯을 레이아웃에 추가

        save_button = Button( #Button 위젯 생성
            text="저장버튼이에요..", # "저장버튼이에요" 이라는 버튼의 레이블 설정
            on_press=self.save_memo # on_press 속성에 버튼 눌렀을때 self.save_memo 함수를 연결함
            ) 
        self.add_widget(save_button) # save_button을 레이아웃에 추가

    def save_memo(self, instance):
        memo = self.memo_input.text # memo_input에 입력된 메모를 가져와 memo 변수로 지정
        print("메모가 저장됨!!:", memo) # 콘솔에 memo를 출력
        self.memo_input.text = "" # 변수 초기화

class First_MemoAppApp(App):
    def build(self):
        return MemoLayout()

if __name__ == "__main__":
    First_MemoAppApp().run()