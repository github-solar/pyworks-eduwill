#py09일이론01:람다01
#매개변수 1개인 경우

oneup = lambda x : x + 1
print('oneup : ',oneup(1))

#위의 람다식을 한 줄로 간결하게 선언
print((lambda x : x+1)(3))

#위의 람다식으로 일반함수로 선언
def oneup2(x) :
    return x + 1

print('oneup2 : ',oneup2(2))


# 3의 배수를 계산하는 함수
times = lambda n : n*3
print(times(3))
print((lambda n : n*3)(3))
