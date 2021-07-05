#12일이론
#정규표현식
import re

str = "Two is too."
f1 = re.findall("T[ow]o", str) # findall() 은 대소문자를 구별한다.
print(f1)

f2 = re.findall("T[ow]o", str, re.IGNORECASE) #findall() 에서 대소문자 구별하지 않도록 옵션 설정
print(f2)

f3 = re.findall("t[^w]o", str, re.IGNORECASE)
print(f3)






