# 영어 단어 저장 파일 생성

f = open("words.txt", 'w')
word = ['sky', 'sea', 'earth', 'moon', 'tree', 'flower', 'grape', 'strawberry']

for i in word:
    f.write(i + ' ')
f.close()