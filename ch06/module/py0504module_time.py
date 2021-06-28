#05이론02
import time

print(time.time()) #1970년 1월 1일 자정이후부터 초단위 누적값
print(time.localtime())
print(time.ctime()) #날짜와 시간 요일 표시
print(time.strftime('%x', time.localtime()))
print(time.strftime('%c', time.localtime(time.time())))

#중요 time.sleep(1) : 1초간 대기
#주의 파이썬에서는 1초를 1로 표기. 다른 언어는 1000ms로 표기


for i in range(1, 11):
    print(i)
    time.sleep(1)

    

