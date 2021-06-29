
def incrementor(n):
    return lambda x : x + n

#일반함수와 융합해서 선언. 이 연산은 어떻게 되냐?
f = incrementor(10)
print(f(1))
print(f(2))