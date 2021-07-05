#12일이론
#정규표현식
import re
p = re.compile('[a-z]+')
m = p.match('afternoon')
print(m)