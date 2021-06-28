#0408 전역변수의 사용 (정적변수) - 누적값을 공유하는 변수
# global 키워드 선언

'''
def one_up():
    x = x + 1
    return x

x = 0
print(one_up())

이 처럼 전역변수 선언하지 않으면 에러가 뜬다.
'''
    

def one_up():
    global x # 전역변수로 선언하면 정상 작동
    x = x + 1
    return x

x = 0
print(one_up())
print(one_up())
print(one_up())
