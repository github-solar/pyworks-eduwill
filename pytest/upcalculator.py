class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator:

    def minus(self,val):
        self.value -= val

cal = UpgradeCalculator(Calculator)
cal.add(15)
cal.minus(6)

print(cal.value)