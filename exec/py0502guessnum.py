#05일연습02 : 모듈_숫자추측게임

import random

con = random.randint(1, 45) # 파이썬이 추측한 숫자

while True:
    guess = int(input("맞혀보세요(1~45): ")) # 유저가 추측한 숫자

    if guess > con:
        print("작은 수를 입력하세요.")
    if guess < con:
        print("큰 수를 입력하세요.")
    if guess == con:
        print("정답입니다.")
        break
        
    


