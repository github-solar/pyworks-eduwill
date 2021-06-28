# 랜덤하게 거북이가 방황하기

import turtle as t
import random as r

t.shape('turtle')
t.speed(5)
t.bgcolor('lightpink')
t.setup(500, 500) # 작업영역의 크기 설정

for x in range(100):
    angle = r.randint(2, 270)
    t.setheading(angle)
    t.forward(r.randint(33, 100))
