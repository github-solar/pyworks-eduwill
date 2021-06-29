# 영어 타자 연습 프로그램
import random
import time

f = open('words.txt', 'r')
word = f.read().split() # 리스트 형태로 가져옴
#print(word) 정상 출력 확인
f.close()

n = 1
print('[타자 게임]준비되면 엔터')
input()
start = time.time()
q = random.choice(word) # 단어 램덤 선택

while n <= 10:
    print('문제', n)
    print(q)
    x = input() # 사용자가 문자 입력
    if q == x:
        print('통과!')
        n = n + 1
        #q 그냥 q로 정의하면 안된다.
        q = random.choice(word)
    else:
        print('오타 다시도전')

print('게임종료')
end = time.time()
et = end - start
print('타자 시간 : %.2f초' % et)