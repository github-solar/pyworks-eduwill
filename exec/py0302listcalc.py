# 연습 3일차01 :리스트 for문 응용
# 60점이상이면합격 아니면 불합

print("for - in 문 계산")
score = [79, 80, 50, 60, 90, 45]
index = 0

for i in score:
    index += 1 # 이 증감식 없을때 출력결과와 비교
    if i >=60:
        
        print("%d번 학생은 합격입니다." % index)
    else:
        print("%d번 학생은 불합격입니다." % index)

print('='*40)

print("for - in range()문 계산")

n = len(score)
for i in range(0, n):
    if score[i] >= 60: #range는 배열의 순서값(=위치값)이 아니고 배열의 값자체를 반환받는다.
        print("%d번 학생은 합격입니다." % (i+1)) # 대응변수가 식이 되면 i+1 을 괄호로 묵어준다.
    else:
        print("%d번 학생은 불합격입니다." % (i+1))
        
        
    
        
