import re

str = 'park 010-1234-5678'
pat = re.compile('(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)')
#m= re.search(pat, str)
#print(m.group(0)) #전체 문자열 반환
#print(m.group(1)) #전체 문자열 반환
#print(m.group(2)) #전체 문자열 반환

#sub 메서드 사용

#s= pat.sub("\g<name>  \g<phone>", str)
pat = re.compile('(\w+)\s+(\d+[-]\d+[-]\d+)')
s= pat.sub("\g<2> \g<1>", str) #이것은 참조번호를 사용
print(s)
