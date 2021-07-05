#12일이론
#정규표현식
import re
p = re.compile('a.b')
m = p.match('a3b')
print(m)