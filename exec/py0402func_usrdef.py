#04일07 abs() 직접정의해주자_함수로

import math
def abs_sign(x):  

    if x < 0:
        x = -(x)

    elif x >= 0:
        x = x
    return x


# 방법2-제곱근을 구해도 절대값이 나온다.

def abs_sign2(x):
    return math.sqrt(x*x) #이것은 제곱근값을 구하는 수학메서드 


n1 = abs_sign(-3)
print(n1)

n2 = abs_sign2(-7)
print(n2)


