#연습:자리배치도
#입장객 수에 따른 좌석 줄 수의 개수 계산하기

customer_num = int(input("입장객 수 입력 : "))
col_num = int(input("좌석 열의 수 입력: "))


if customer_num % col_num == 0:
    row_num = int(customer_num / col_num) #여기를 //로 연산해보자.
    # 나머지는 결과값이 실수이므로 정수로 형변환 필요.
else:
    #row_num = int(customer_num / 
    #row_num = int(customer_num / col_num + 1
    row_num = int(customer_num // col_num) + 1


print("%d개의 줄이 필요합니다." % row_num)

print("자리 배치도")
for i in range(0, row_num): #이것은 행을 추출하는 반복문이다.
    for j in range(1, col_num+1): #이것은 열을 추출하는 반복문이다.
        seat_num = i*col_num+j
        print(seat_num, end=' ')
        if seat_num >= customer_num:
            break;
    print()
