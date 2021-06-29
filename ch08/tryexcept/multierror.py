
try:
    a = [1, 2]
    print(a[2]) # 에러가 난다.

except IndexError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
    