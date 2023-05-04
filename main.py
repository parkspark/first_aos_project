from kivy.app import App
from kivy.uix.label import Label
from kivy.core.text import LabelBase, DEFAULT_FONT # font
from kivy.resources import resource_add_path # font
from kivy.uix.boxlayout import BoxLayout # ui
from kivy.uix.textinput import TextInput # ui
from kivy.uix.button import Button # ui
import os # 메모 삭제때 os.remove 이용하려고 임포트

resource_add_path('.')
LabelBase.register(DEFAULT_FONT, "./MaruBuriTTF/MaruBuri-Regular.ttf")

# class KivyMemoApp(App):
#     def build(self):
#         return Label(text="메모장 어플 입니다!")

class MemoLayout(BoxLayout): # BoxLayout을 상속받아 앱의 레이아웃 정의
    def __init__(self, **kwargs):
        super(MemoLayout, self).__init__(**kwargs)
        self.orientation = "vertical" #orientation 속성을 vertical로 설정 : 위에서 아래로 위젯 배치

        self.memos = {} #메모를 저장할 딕셔너리 <- 왜 딕셔너리?

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
        
        #ID 입력 textinput
        self.memo_id_input = TextInput(hint_text = "메모 ID 입력", multiline = False, size_hint_y=None, height=30)
        self.add_widget(self.memo_id_input)

        #CRUD 버튼
        button_layout = BoxLayout(size_hint_y=None, height=30)
        self.add_widget(button_layout)

        read_button = Button(text="읽기", on_press=self.on_read_button) #read
        button_layout.add_widget(read_button)

        update_button = Button(text="수정", on_press=self.on_update_button) #update
        button_layout.add_widget(update_button)

        delete_button = Button(text="삭제", on_press=self.on_delete_button) #delete
        button_layout.add_widget(delete_button)
        
    # 각 버튼에 대한 콜백함수
    def on_read_button(self, instance):
        memo_id = int(self.memo_id_input.text)
        self.read_memo(memo_id)

    def on_update_button(self, instance):
        memo_id = int(self.memo_id_input.text)
        new_memo = self.memo_input.text
        self.update_memo(memo_id, new_memo)
        self.memo_input.text = ""

    def on_delete_button(self, instance):
        memo_id = int(self.memo_id_input.text)
        self.delete_memo(memo_id)
        self.memo_id_input.text = ""

    def save_memo(self, instance):
        memo_id = len(self.memos) + 1 #새 메모 id생성
        memo = self.memo_input.text # memo_input에 입력된 메모를 가져와 memo 변수로 지정
        self.memos[memo_id] = memo # 메모를 딕셔너리에 추가
        
        with open(f"memo_{memo_id}.txt", "w", encoding="utf-8") as memo_file:
            memo_file.write(memo + "\n")        
        print("메모가 저장됨!!:", memo) # 콘솔에 memo를 출력
        self.memo_input.text = "" # 변수 초기화
        
    def read_memo(self, memo_id):
        if memo_id in self.memos:
            print(f"메모 {memo_id}: {self.memos[memo_id]}")
        else:
            print(f"입력하신 {memo_id}의 메모가 존재하지 않습니더..")
    
    def update_memo(self, memo_id, new_memo):
        if memo_id in self.memos:
            self.memos[memo_id] = new_memo

            with open(f"memo_{memo_id}.txt", "w", encoding="utf-8") as memo_file:
                memo_file.write(new_memo)
                
            print(f"메모 {memo_id}가 수정 됨!")
        else:
            print(f"입력하신 {memo_id}의 메모가 존재하지 않습니더..")
    
    def delete_memo(self, memo_id):
        if memo_id in self.memos:
            del self.memos[memo_id]
            memo_file = f"memo_{memo_id}.txt"
            if os.path.exists(memo_file):
                os.remove(memo_file)            
            print(f"메모 {memo_id}이(가) 삭제되었습니다.")
        else:
            print(f"입력하신 {memo_id}의 메모가 존재하지 않습니더..")
            
class First_MemoAppApp(App):
    def build(self):
        return MemoLayout()

if __name__ == "__main__":
    First_MemoAppApp().run()