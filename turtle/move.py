import turtle as t
import random as r

t.shape('turtle')
t.speed(0)
t.up()
#t.goto(0, -200) # 화면 출력시 초기 위치값 선언
x = r.randint(-230, 230)
y = r.randint(-230, 230)
t.goto(x, y)
t.mainloop()