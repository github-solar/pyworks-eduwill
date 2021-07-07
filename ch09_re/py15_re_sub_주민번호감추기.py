import re

data = """          
kim 871111-1234567
lee 861231-2234567
"""
#중요기본) 변수를 여러개 담을 때 구문형식 """ ~ """

pat= re.compile("(\d{6})[-]\d{7}")
m= pat.sub("\g<1>-*******", data)
print(m)