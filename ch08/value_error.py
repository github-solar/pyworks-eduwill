#에러처리:컴퓨터 뻑될 때 빠져나오도록
#try: ~ except ValueError as e: ~ print(e) <- 이렇게 선언해도 되지만 아래처럼 설명문을 출력하도록
while True:
    try:
        x = int(input("숫자를 입력하세요 : "))
        print(x)
        break
    except ValueError as e:
        #print(e)
        print('숫자형식이 아닙니다. 숫자를 입력하세요. ')
