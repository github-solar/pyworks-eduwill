#12일이론
#정규표현식
import re #re는 정규표현식을 불러오는 지정어
p = re.compile('[a-z]+') # +는 반복을 의미하는 메타 문자
m = p.match('afternoon')
print(m)