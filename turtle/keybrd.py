import turtle as t

def turn_rgt():
    t.setheading(0)
    t.forward(10)

def turn_up():
    t.setheading(90)
    t.forward(10)

def turn_lft():
    t.setheading(180)
    t.forward(10)

def turn_dwn():
    t.setheading(270)
    t.forward(10)

def clear():
    t.clear()


t.shape('turtle')
t.onkeypress(turn_rgt, "Right")  #키보드 화살표키와 연동
t.onkeypress(turn_up, "Up")  #키보드 화살표키와 연동
t.onkeypress(turn_dwn, "Down")  #키보드 화살표키와 연동
t.onkeypress(turn_lft, "Left")  #키보드 화살표키와 연동
t.onkeypress(clear, "Escape")
t.listen() #키보드의 동작을 기다린다.

t.mainloop()