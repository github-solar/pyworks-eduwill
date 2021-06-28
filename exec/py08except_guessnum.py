#05일연습02 : 모듈_숫자추측게임

import random as r

con = r.randint(1, 45) # 파이썬(또는 프로그램)이 추측한 숫자

while True:
    try:

        guess = int(input("맞혀보세요(1~45): ")) # 유저가 추측한 숫자

        if guess > 45 or guess < 1:
            print('입력범위를 초과했으니 다시 입력하세요.')
        elif guess > con:
            print("작은 수를 입력하세요.")
        elif guess < con:
            print("큰 수를 입력하세요.")
        else:
            print("정답입니다.")
            break



    except ValueError:
        print('숫자가 아닙니다. 다시 입력해주세요.')


        
    


