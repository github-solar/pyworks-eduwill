from tkinter import *

def click():
    en_text = entry.get()
    name = en_text + "님 Hello~ Python!!"
    text.insert(END, name)

root = Tk()
root.title("Hello~") #루트
root.geometry("300x100+200+200")

frame = Frame(root) #프레임
frame.pack()

Label(frame, text="이름 : ").grid(row=0, column=0)
entry = Entry(frame, width=10) #입력받기 창이다.
entry.grid(row=0, column=1)

Button(frame, text="확인", command=click).grid(row=1, columnspan=2)
#click()으로 선언하지 않은 이유? 버튼 누를 때만 클릭 함수가 작동해야 한다. ()을 넣으면 앱구동 초기부터 함수가 작동한다.
text = Text(frame, width=10, height=5) #값은 칼럼수와 로우수로 봐라.
text.grid(row=2, columnspan=2)


root.mainloop()