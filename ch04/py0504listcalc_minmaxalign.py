# 리스트의 최대값, 최소값, 정렬

score = [79, 80, 50, 60, 90, 45]

max = score[0]
n= len(score)


for i in range(1,n):
    if score[0] < score[i]:
        max = score[i]
print('최대값 : ', max)

print('='*50)

#간단하게 정렬하는 방법은 sort()메서드를 호출한다. 다만 구문형식을 주의하라.
score.sort() #먼저 메서드를 써서 리스트를 정렬하고 이것은 오름차순
print('sort()함수 오름차순 정렬 : ', score) #출력해본다.

score.reverse()
print('reverse()함수 내림차순 정렬 : ', score)

print('='*50)


#알로리즘을 짜서 오름차순 정렬하기 : 이거 생각할 알고리즘 과정이 길다.
#리스트 요소를 순차정렬하려면 반드시 행렬을 생성하고 변수 교환까지 짜야 한다.

for i in range(0, n):
    for j in range(0, n-1):
        if score[j] > score[j+1]:
            score[j], score[j+1] = score[j+1], score[j]

print('알고리즘 오름차순 정렬 : ', score)

print('='*50)


'''
반복문 수행과정 추
#1행
79, 50, 60, 80, 45, 90
#2행
50 60 79 45 80 90
#3행
50 60 45 79 80 90
#4행
50 45 60 79 80 90
#5행
45 50 60 79 80 90 : 완성
'''



               
               
