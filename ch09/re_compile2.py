#12일이론
#정규표현식
import re
p = re.compile('[a-z]+')
m = p.match("2021 incheon") #이 명령문은 처음에 일치하는 문자가 없어서 none 결과
print('p.match로 검색 :', m)

s = p.search("2021 incheon") # 전체로 검색해서 일치된 문자를 검색
print('p.search로 검색 :', s)