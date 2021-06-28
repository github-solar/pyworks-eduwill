#연습04 p.112~
#1번
국어 = 80
영어 = 75
수학 = 55

sum = 국어 + 영어 + 수학
avg = sum / 3

print("과목 평균은 ", avg, "입니다.")

#2번
print(13 % 2)

n = 13

if n % 2 == 0:
    print("짝수")
else:
    print("홀수")

#3번
pin = "881120-3068234"
yyyymmdd = pin[0:6]
num = pin[7:]

print(yyyymmdd)
print(num)

#4번
sex = pin[7]
#print('성별은 : ', sex)

if sex == "1" or "3":
    print("남자 입니다.")
else:
    print("여자 입니다.")

#5번
a = "a:b:c:d"
b = a.replace(':','#')
print(b)

#6번
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

#7번
a = ['Life', 'is', 'too', 'short']
result = ' '.join(a)
print(result)

print('='*50)

#7번 split
s = "Life is too short"
#s.split()
msg=s.split(" ") #split함수를 써서 list로 출력하려면 이 값을 변수에 담아라.
 
print(msg)

a = "a:b:c:d"
a = a.split(':')
print(a)

print('='*50)

#8번 튜플
a = (1, 2, 3)
a = a + (4,) 
print(a)

print('='*50)

#9번
a = dict()
a
a['name'] = 'python'
print(a)
a[('a',)] = 'python'
print(a)

#a[[1]] = 'python' #여기서 에러가 뜨긴 하는데 ....
#print(a)

a[250] = 'python'

print('='*50)

#10번
a = {'A':90, 'B':80, 'C':70}
result = a['B']
print(a)
print(result)

#11번
a = [1,1,1, 2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)

print('='*50)

#12번
a = b = [1,2,3]
a[1] = 4
print(a)

print(b)

print('='*50)






