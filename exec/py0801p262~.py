#1번
class Calculater:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value

class UpgradeCalculater(Calculater):
    def minus(self, val):
        self.value -= val
        return self.value

# 2번
class MaxLimitCalculater(Calculater):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100
        return self.value

c = Calculater()
c.add(10)
print(c.value)

cal = UpgradeCalculater()
cal.add(10)
cal.minus(7)
print(cal.value)

cal2 = MaxLimitCalculater()
print(cal2.add(50))
print(cal2.add(60))
print(cal2.value)

#3번

#4번
li = [1, -2, 3, -5, 8, -3]

#print(list(filter(lambda x : x >=0, li)))

#4번을 일반함수로

def over0(a):
    a2=[]
    for i in a:
        if i >= 0:
           a2.append(i)
    return a2

li2 = over0(li)
print(li2)

#6번
li = [1,2,3,4]
#print(list(map(lambda x : x *3, li)))

#일반함수로
def times(a):
    a2 = []
    for i in a:
        a2.append(i*3)
    return a2
li2 = times(li)
print(li2)

#7번
d1 = [-8, 2, 7, 5, -3, 5, 0, 1]

max = max(d1)
min = min(d1)

print(max)
print(min)
print(max + min)

#7번 메소드로
def find_max(li):
    max = li[0]
    n = len(li)
    for i in range(n):
        if max < li[i]:
            max = li[i]

    print(max)
    return max

'''
n = len(li)
for i in range(1, n)
    print(max)
    
'''
max2 = find_max(d1)

print("함수로 최대값", max2)


#12번
import time
import datetime

now = time.strftime("%Y/%M/%d %H:%M:%S")
print(now)

now2 = datetime.datetime.now()
print(now2.strftime("%Y/%M/%d %H:%M:%S"))






