#이론 중첩for문
#5행 5열 배열
for i in range(1, 6):
    for j in range(1, 6):
        print("가", end=' ')
    print()


for i in range(0, 5):
    for j in range(1, 6):
        num = i*5+j
        if i < 2:
            print(num, end='  ')
        else:
            print(num, end=' ')
            
    print()
