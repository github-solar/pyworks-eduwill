#연습 p146~

#1번
print('1번')
a = "Life is too short, you need python"

if "wife" in a:
    print("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a:
    print("shirt")
elif "need" in a:
    print("need")
else:
    print("none")

print('='*50)
    

#2번
print('2번')
result = 0
i = 1
while i<= 1000: 
    if i % 3 == 0:
        result += i
    i += 1
print(result)

print('='*50)




#3번
print('3번-기본풀이')

i = 0

while True:
    i +=1
    if i > 5:
        break
    print("*"*i)

print('='*50)


print('3번-이중for문')

#3번을 이중 for문
for i in range(1, 6):
    for j in range(1, i+1):
        print('*', end='')
    print()

print('='*50)

    


#4번
print('4번')

for i in range(1,101) :
    print(i)

print('='*50)


#5번
a = [70,60,55,75,95,90,80,80,85,100]

total = 0
for score in a:
    total += score
average = total / len(a)
print(average)

print('='*50)

#6번
nums = [1, 2, 3, 4, 5]

result =[]
for n in nums:
    if n % 2 == 1:
        result.append(n*2)

print(result)

#리스트 내포
#조건문을 간단하게 선언하는 구문 같다. 매우 간단하다.

result2 = []
result2 = [n*2 for n in nums if n % 2 == 1]
print(result2)
        




        



    


    
    
    
        
    
    
    
    
    
    
    
    
    
