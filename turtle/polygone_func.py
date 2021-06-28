#다른 곳에 도형 그리기_함수로 매개변수 1개짜리 2개짜리
import turtle as t

t.shape('turtle')

def polygon(n):
    for x in range(n):
        t.forward(50)
        t.left(360/n)

def polygon2(n, d):
    for x in range(n):
        t.forward(d)
        t.left(360/n)

        

polygon(3)

polygon(5)
    

t.up() # 선 올리기
t.back(100) #100px 만큼 뒤로 이동
t.down() # 선 내리기


polygon2(4, 80)
polygon2(5, 97)
    
t.mainloop()