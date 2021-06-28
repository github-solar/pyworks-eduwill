class Calculater:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value +=val

class UpgradeCalculater:
    def __init__(self):
        self.value -= val

cal = UpgradeCalculater(Calculater)
cal.add(10)
cal.add(20)
print(cal.value)

