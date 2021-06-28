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

def start():

    global playing #전역변수로 형변형

    if playing == False:
        playing = True
        t.clear()
        play()

def message(m1, m2):
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, "center", ("",20))
    t.goto(0, -100)
    t.write(m2, False, 'center', ("",15))

def play():
    global score
    #global playing
    t.forward(10)


    if random.randint(1, 5) == 3:
        ang = te.towards(t.pos())
        te.setheading(ang)
    speed = score + 5

    te.forward(speed)

    if t.distance(tf) < 12:
        score +=1
        t.write(score)
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        tf.goto(x,y)

    if t.distance(te) < 12:
        text = "score : " + str(score)
        message("Game Over", text)
        playing = False
        score = 0


    if playing:
        t.ontimer(play, 100)

#메인 영역
#점수 변수와 플레이 스위치(bool) 변수 선언
score =0
playing = False
t.setup(500, 500) #너비, 높이
t.title('달려라 거북이')
t.bgcolor("orange")
t.shape('turtle')
t.speed(0)
t.up()
t.color("white") # 주인공 거북이 설정

#적 터틀
te = t.Turtle() # Turtle 클래스에서 te 인스턴스 생성
te.shape('turtle')
te.color('red')
te.speed(5)
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
t.onkeypress(start, "space")  #키보드 화살표키와 연동

t.listen() #키보드의 동작을 기다린다.
message('Turtle Run', '[space]')

t.mainloop()
