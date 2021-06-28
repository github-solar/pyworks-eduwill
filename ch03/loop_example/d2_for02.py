#이론:for 구구단 단을 입력받아 출력하기

dan = int(input("단을 입력하세요 : "))
for i in range(1,10):
    print("%d X %d = %d" % (dan, i, dan*i))
