import re

p = re.compile("(\w+)\s+(\d+[-]\d+[-]\d+)")
s = p.search("jang 010-1234-5678")
print(s.group(1))
print(s.group(2))
#정규표현식의 match, search 객체의 특유의 메서드(=함수)로 group()이 있다. 다른 것도 있다.
#즉, group()메서드는 정규표현식의 여러 개체에서 쓰이는 메서드가 아니다.
