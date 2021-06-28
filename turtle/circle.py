#여러 개의 원 만들기
import turtle as t

n = 50
t.speed(0) # speed개체는 0~9까지 단계조절되고 0이 가장 빠르다.
t.color('red')
t.bgcolor('black')

for x in range(n):
    t.circle(80)
    t.left(360/n)
