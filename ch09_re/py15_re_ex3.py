import re

str = "abcd<hr>Thank you"
pat = re.compile("(<.+>)") #태그까지 추출하려고 할때
#pat = re.compile("<(.+)>)") #태그를 제외하고 추출하려고 할때
m= re.findall(pat, str)
print(m)

