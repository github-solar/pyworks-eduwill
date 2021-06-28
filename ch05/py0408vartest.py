#04 var 전역변수와 지역변수

a = 1

def vartest(a):
    #global a # 이렇게 전역변수로 지정하면 값이 누적된다.
    # 전역변수를 선언하면 위에 파라메터 a는 삭제해야 에러가 안난다.
    a = a + 1 #여기는 지역변수다.
    return a


a = 1 # 이것은 전역변수다. 즉 위와 아래의 a는 동일한 값이 아니다.

print(vartest(a))
print(a)

    
