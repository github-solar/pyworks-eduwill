import random
import turtle as t
import random as r

def turn_rgt():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_lft():
    t.setheading(180)

def turn_dwn():
    t.setheading(270)


def play():
    t.forward(10)
    te.forward(9)

    #적 거북이가 먹이에 닿으면 먹이가 램덤하게 이동
    if t.distance(tf) < 12:
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        tf.goto(x,y)

    ang = te.towards(t.pos())
    te.setheading(ang)

    if t.distance(te) >=12: #거리가 12보다 작으면 잡혀서 게임 종료
        t.ontimer(play, 100) #0.1초

t.setup(500, 500)
t.title('달려라 거북이')
t.bgcolor("orange")
t.shape('turtle')
t.speed(0)
t.up()
t.color("white") # 주인공 거북이 설정

te = t.Turtle() # Turtle 클래스에서 te 인스턴스 생성
te.shape('turtle')
te.color('red')
te.speed(0)
te.up()
te.goto(0, 200)

tf = t.Turtle()
tf.shape('circle')
tf.color('green')
tf.speed(0)
tf.up()
tf.goto(0, -200)
t.onkeypress(turn_rgt, "Right")  #키보드 화살표키와 연동
t.onkeypress(turn_up, "Up")  #키보드 화살표키와 연동
t.onkeypress(turn_dwn, "Down")  #키보드 화살표키와 연동
t.onkeypress(turn_lft, "Left")  #키보드 화살표키와 연동

t.listen() #키보드의 동작을 기다린다.

play()

t.mainloop()
