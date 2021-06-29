#파일 불러오기. 내용 출력 추출. 그리고 반드시 에러처리 구문 선언할 것
try:
    f = open('e:/python/pyworks-jds/pyfile/hello.txt', 'r')
    data = f.read()
    print(data)
    f.close()
except FileNotFoundError:
    print('파일을 찾을 수 없습니다.')