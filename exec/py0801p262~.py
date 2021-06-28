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


