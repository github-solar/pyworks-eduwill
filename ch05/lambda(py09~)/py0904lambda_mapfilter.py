li = [1, 2, 3, 4, 5]

#람다식의 map()함수 연습. 매핑(지정한 조건에 맞추어 원본값을 가공 계산한다.)
li2 = map(lambda x : x * 3, li)

print(list(li2))
#한줄로 표현
print(list(map(lambda x : x * 3, li)))

#람다식의 filter()
li3 = filter(lambda x : x < 4, li)
print(list(li3))
print(list(filter(lambda x : x < 4, li)))