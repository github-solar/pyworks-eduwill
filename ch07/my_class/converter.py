#07일01연습 클래스 실습 단위변환 실습에서 자주 나오는 문제유형

class Scalecnvter:
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from
        self.units_to = units_to
        self.factor = factor

    def convert(self, val): # self.factor : 25
        return self.factor * val

if __name__=='__main__':
c1 = Scalecnvter('inches', 'mm', 25)
print('converting 2 inches')
print(str(c1.convert(3)) + c1.units_to)
#위에 왜 str으로 형변환 하는지 그 이유를 알아야 한다.
