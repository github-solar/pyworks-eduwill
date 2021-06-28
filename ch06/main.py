from my_module.math.calculator import add, sub, mul, div
#사용자 정의 모듈에서 특정 def 를 호출하는 구문이다.
add = add(10,4)  #여기서 앞의 add는 이 파일에서의 변수이고
sub = sub(10,4)  #뒤의 add()는 사용자 정의 모듈의 함수이름이다. 따라서 같아도 오류는 없다.
mul = mul(10,4)
div = div(10,4)

print(add)
print(sub)
print(mul)
print(div)

