#04일03 자료구조_딕셔너리

person = {}

print(person)

person['name'] = '이순신'
person['age'] = 40

print(person)

person['addrs'] = '전라남도'

#dic의 value 출력
for key in person:
    print(person[key])

#요소 삭제 : dic.pop('addrs')와 같음. .pop()은 함수를 써서 삭제
del person['addrs']
print(person)

    
    
