#04일연습02 함수

#도형의 면적을 계산하는 함수 정의와 사용

def squre(w, h):
    area = w * h
    return area
def triangle(n, h):
    area2 = (n * h) / 2
    return area2

print('사각형의 면적 : ', squre(5, 4))
print('삼각형의 면적 : ', triangle(4, 7))
