import random

# 주사위 10회 던지기
dice = []
for i in range(0, 10):
    n = random.randint(1, 6)
    dice.append(n)

print(dice)

# 로또 복권 생성기
lotto = []
for i in range(6):
    print(len(lotto))
    n = random.randint(1, 45)
    if n not in lotto: # 중복된 번호는 생략하라.
        lotto.append(n)

print("for문으로 로또번호 추출 : ", lotto)
#다시 한 결과 for문을 n으로 하니까 중복번호가 안나오는 것 같다.
#다만 n으로 선언하면 로또번호가 6개미만으로 생성될 수 있다.
#for문으로 중복되지 않게 6개를 뽑으려고 알고리즘을 짜면 오류가 생긴다.
#그래서 이를 방지하고자 while 문으로 쓴다.

lotto2 = []
while len(lotto2) < 6:
    print(len(lotto2))
    n = random.randint(1, 45)
    if n not in lotto2: # 중복된 번호는 생략하라.
        lotto2.append(n)

print("while문으로 로또번호 추출 : ", lotto2)