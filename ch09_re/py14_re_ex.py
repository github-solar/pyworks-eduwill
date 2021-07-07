# 정규표현식의 *, + 의 차이
import re
pat = re.compile("ca*t") # * 는 앞문자가 0개 이상 반복 (없어도 가능하다.)
m1 = re.findall(pat, 'caat')
print(m1)

m2 = re.findall(pat, 'ct')
print(m2)

pat2 = re.compile("ca+t") # + 는 앞문자가 1개 이상 반복
m3 = re.findall(pat2, 'caat')
print(m3)

m4 = re.findall(pat2, 'ct')
print(m4)

#compile()메소드는 바이트코드로 변환되어 속도가 빠르다. 데이터가 많을 때는 compile()메소드를 활용.
#