#리스트를 매개변수로 전달하기
#점수의 평균 계산하기

def avg(a):

    sum = 0
    c = len(a)
    for i in a:
        sum += i
    avge = sum / c
    print("학생 수 : ", c) # 학생수 출력함수 위치를 잘 잡아야 한다.      
    return avge 

kor = [70, 80, 60, 90, 100]
avg = avg(kor)


print('평균 점수 : ', avg)
