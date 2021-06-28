#연습02 : 입력받아 넓이 구하기
# 입력받아서 넓이값 구하기
# 정사각형 넓이  
print('정사각형 넓이 구하기')
size = int(input('한 변의 길이 : '))

area = size**2

print('정사각형의 넓이 : ', area, 'cm2')
print('정사각형의 넓이 : %d ㎠' % area)


# 삼각형의 넓이
print('삼각형 넓이 구하기')

width = int(input('밑변의 길이 : '))
height = int(input('높이 : '))

area2 = (width * height) / 2

print('삼각형의 넓이 : ', area2, '㎠')
print('삼각형의 넓이 : %d ㎠' % area2)

# 위처럼 쓰면 소수점 이하가 표기되지 않는다. 해결책을 찾을 것. 
