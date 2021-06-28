cust_num = input('전체 인원수 : ')
col_num = input('좌석 열수 : ')

if int(cust_num) % int(col_num) == 0:
    row_num = int(cust_num) / int(col_num)
else:
    row_num = (int(cust_num) // int(col_num)) + 1


print('필요한 줄 수 : ', row_num)

