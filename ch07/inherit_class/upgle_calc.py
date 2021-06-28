from ch07.my_class.calculator import Calculator
# Calculater 를 확장한 MoreCalculator 클래스 생성하기

class MoreCalculator(Calculator):
    def pow(self):
        return self.x ** self.y

    def div(self): # 나눗셈에서 0으로 나누면 연산이 죽는다. 컴퓨터 다운 이것을 빠져나오는
        if self.y == 0 :
            return 0
        else:
            return self.x / self.y


cal = MoreCalculator(3, 0)

print(cal.add())
print(cal.sub())
print(cal.mul())
print(cal.div())
print(cal.pow())
