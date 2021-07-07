
#sum = 0
def hap():
    sum = 0
    for i in range(1, 11):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i
            print(i) #print(i) 이 위치에서 선언될 때
        #print(i) #print(i) 이 위치에서 선언될 때 위와 아래의 차이점은?
    return sum

total = hap()

print(total)

