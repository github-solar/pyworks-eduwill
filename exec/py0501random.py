#05일연습01 랜덤

# 주사위 2개 10번 던지기

import random

for i in range(10):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2
    print(total)
    

    if total == 7:
        print('seven Thrown!!')
    if total == 11:
        print('Eleven Thrown!!')
    if dice1 == dice2:
        print('Double Thrown!!')
        
        
