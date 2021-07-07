#12일이론
#정규표현식
import re
p = re.compile('a.b')
m = p.match('a3b') #match()는 처음부터 문자를 검색한다. = find()와 비슷
print(m)            #findall()은 전체를 검색해서 리스트로 반환 = findall()과 비슷