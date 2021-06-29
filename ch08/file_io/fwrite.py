# 파일 열기(open()) -> 파일 쓰기(write() -> 파일 닫기(close())

f = open('e:/python/pyworks-jds/pyfile/hello.txt', 'w')
f.write('hello python')
#f.write(1000) 에러뜬다. 숫자 입력은 포맷 방식으로 입력해야 한다.
#f.write("\n %d" % 100) # 파일에 숫자를 입력할 때
f.write("%.1f\n" % 7.3)
num = "%d" % 100000
f.write(num)
f.write('안녕~ 파이썬')
f.close()