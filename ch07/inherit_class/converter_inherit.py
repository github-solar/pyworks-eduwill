#08일이론01: 상속실습 계속
from ch07.my_class.converter import Scalecnvter
#단위변환 클래스확장
#온도 변환

class Converters(Scalecnvrter):
    def __init__(self, units_from, units_to, factor, offset):
        super().__init__(units_from, units_to, factor)
        self.offset = offset

    def convert(self, val):
        return self.factor *val + self.offset

con = Converters('C', 'F', 1.8, 32)
print("Converting 23C")
print(str(con.convert(23) + con.units_to)