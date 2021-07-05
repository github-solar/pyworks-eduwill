#윈도우(폼) 만들기

from tkinter import *  #티킨터 내의 모든 모듈을 가져온다.

root = Tk() # Tk() 클래스의 객체 생성
root.title("window")
root.geometry("640x480+300+400") #폼의 가로세로 화면크기 설정 또는 선언 그리고 좌표값 설정법

frame = Frame(root) # root 바탕 위에 위치하는 프레임 위치
frame.pack() #레이아웃을 담당하는 메서드

# 문자열을 출력 - label 클래스
Label(frame, text="hello python").grid(row=0, column=0)

# 버튼 클래스
Button(frame, text="확인").grid(row=1, column=0)

root.mainloop()