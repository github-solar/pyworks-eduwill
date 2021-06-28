#연습: 윤년 판별 프로그램

year = int(input("년도를 입력하세요 : "))

'''
if year % 4 == 0:
    print("윤년 입니다.")
elif year % 400 == 0:
    print("윤년 입니다.")
elif year % 4 == 0 and year % 100 == 0:
    print("평년 입니다.")
else:
    print("평년 입니다.")


위에 내가 짠 조건식으로 결과값을 얻으면
1500, 1700, 1900 등도 모두 윤년으로 판별된다. 그 이유는?
파이썬은 맨 처음 조건식에 대입해서 맞으면 그 이후 조건식은 고려하지 않는다.
아마도 이것 때문일 것이다.
'''
#수정조건식이다.
'''
if year % 400 == 0:
    print(year, '년은 윤년입니다.')
elif year % 100 == 0 and year % 400 == 0:
    print(year, '년은 평년입니다.')
elif year % 4 == 0:
    print(year, '년은 윤년입니다.')
else:
    print(year, '년은 평년입니다.')

수정조건식도 오류발생한다.
'''
'''
윤년의 조건
4년마다 오며, 100년 단위는 윤년이 아니나, 400년 단위는 윤년이다.
튜터답안
'''
'''
if year % 4 == 0 and year % 100 != 0 and year % 400 == 0:
    print(year, '년은 윤년입니다.')
else:
    print(year, '년은 평년입니다.')

튜터답안도 오류발생한다.
'''

'''
#내가 만든 수정조건식2_성공

if year % 400 == 0:
    print(year, '년은 윤년입니다.')
elif year % 400 == 0 and year % 100 == 0:
    print(year, '년은 평년입니다.')
elif (year % 400 == 0 or year % 4 == 0) and year % 100 != 0:
    print(year, '년은 윤년입니다.')
else:
    print(year, '년은 평년입니다.')

#비로소 수정조건식2 에서 오류없이 윤년 판별이 된다. 성공!!
'''

#강사제시답안 다시_성공. 이게 훨씬 간단하다.

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('윤년 입니다.')
else:
    print('평년 입니다.')
    
    
    
    


    
    
    
