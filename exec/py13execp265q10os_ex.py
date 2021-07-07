import os

'''
os.chdir("c:/")
dir = os.popen('dir')
print(dir)
print(dir.read())
'''
# 디렉터리 명칭을 리스트로 반환받기
dirnames = os.listdir('e:/python/pyworks-jds/exec')
print(dirnames)
print(dirnames[0])
print(dirnames[-1])

for dirname in dirnames:
    print(dirname)


