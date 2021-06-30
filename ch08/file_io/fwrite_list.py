#list 자료 읽기

f = open('e:/python/pyworks-jds/pyfile/2021kbo.txt', 'w')
team = ['기아', '삼성', '쓱', '롯데', '키움']


#for문으로 리스트 자료를 입력
for i in team:
    f.write(i + ' ')
f.close()

'''
# range()함수로 파일에 리스트 자료 입력
n = len(team)
for i in range(n):
    f.write(team[i] + ' ')
f.close()
'''

f = open('e:/python/pyworks-jds/pyfile/2021kbo.txt', 'r')
data = f.read()
print(data)
f.close()