from tkinter import *

def click():
    print("Hello~ Python!!")

root = Tk()
root.title("Hello~") #루트

frame = Frame(root) #프레임
frame.pack()

Button(frame, text="확인", command=click).grid(row=0, column=0)
#click()으로 선언하지 않은 이유? 버튼 누를 때만 클릭 함수가 작동해야 한다. ()을 넣으면 앱구동 초기부터 함수가 작동한다.


root.mainloop()