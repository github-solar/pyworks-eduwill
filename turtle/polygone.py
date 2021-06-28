#다른 곳에 도형 그리기
import turtle as t

t.shape('turtle')

for x in range(4):
    t.forward(100)
    t.left(90)

t.up() # 선 올리기
t.back(100) #100px 만큼 뒤로 이동
t.down() # 선 내리기


for x in range(4):
    t.back(77)
    t.left(90)
    
    
