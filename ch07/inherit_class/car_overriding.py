#Car 클래스(부모) - 택시, 버스 는 자식 클래스 관계에서
# 특히 상속 기법에서 메소드 재정의가 이루어진다. 오버라이딩

class Car:
    def drive(self):
        print('차가 주행합니다.')

class Taxi(Car):
    def drive(self):
        print('택시가 주행합니다.')

class Bus(Car):
    def drive(self):
        print('버스가 주행합니다.')

c = Car()
c.drive()

taxi = Taxi()
taxi.drive()

bus = Bus()
bus.drive()