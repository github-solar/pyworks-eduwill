# try~except~finally

def divide(x, y):
    try:
        div = x / y
        #print(div)
        #return div
    except ZeroDivisionError:
        print('0으로 나눌 수 없습니다.')
    else: # 예외처리에 else: 조건분기문을 넣을 수도 있다. try: 분기문에서 print(div)를 빼고
        print(div)
    finally:
        print('여기는 꼭 수행하는 구간입니다.')

divide(3, 0)