#사용자 입력받아 파일 쓰기

f = open('input.txt', 'a') #파일경로를 지정안하고 파일만 생성할 때 파일의 위치는?
text = input('내용을 입력하세요 : ')
f.write(text)
f.write('\n')
f.close()
