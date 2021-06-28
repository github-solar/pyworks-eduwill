#05일이론03:리스트보완 2중리스트
# 2차원 리스트의 생성과 출력
# list의 크기는 보통 행의 크기를 말한다. 물론 열의 크기도 있다.
li = [
        [10, 20],
        [30, 40],
        [50, 60]
    ]

print('li[0][0] = ', li[0][0])
print('li[0][1] = ', li[0][1])
print('li[1][0] = ', li[1][0])
print('li[1][1] = ', li[1][1])
print('li[2][0] = ', li[2][0])
print('li[2][1] = ', li[2][1])

print('list의 크기(행) = ', len(li)) #len(리스트명) 은 리스트 행 수를 추출한다.

for i in range(len(li)): # 이것은 행의 순서를 인덱싱하는 반복문이다.
    #print(len(li[i]
    for j in range(len(li[i])):
        print(li[i][j], end=' ')
    print()
        
