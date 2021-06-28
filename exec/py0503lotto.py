#05일연습03: 로또번호

import random as r

lotto = []

for x in range(6): # 0 ~ 5
    n = r.randint(1, 45)
    lotto.append(n)

lotto.sort()

print('번호중복되는 리스트 : ', lotto) # 이 알고리즘까지는 번호가 중복된다.

#여기부터 번호가 중복되지 않는 알고리즘으로

lotto2 = []

while len(lotto2) < 6:
    n = r.randint(1, 45)
    if n not in lotto2:
        lotto2.append(n)

    if len(lotto2) == 6:
        lotto2.sort()
        print(lotto2)
    
'''
for x in range(6):
    n = r.randint(1, 45)
    if n not in lotto:
        lotto.append(n)
            if len(lotto) != 6:
                n = r.randint(1, 45)

            if len(lotto) == 6:
                break

                '''


