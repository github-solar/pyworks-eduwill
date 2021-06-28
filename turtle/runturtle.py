import turtle as t # 이것은 모듈명칭을 닉네임화 하는 것과 같다.

t.shape('turtle')

# 사각형 그리기01
'''
명령문으로
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
'''
#for문으로
n = 4
for i in range(n):
    t.forward(100)
    t.right(90)


#이어서 삼각형 그리기
m = 3
t.color('red')
for i in range(m):
    t.forward(100)
    t.left(120)


#원 그리기
t.color('blue')
t.pensize(3)
t.circle(50)

t.mainloop()

# 5각형 6각형 그리기도 된다.
#반복횟수를 변수로 선언하여 값을 변화시킨다.
    
    
    
    
    
        


