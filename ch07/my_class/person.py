# 클래스 생성과 활용
# 이것은 클래스에 하나의 객체만 저장되는 구문형식이다.


class Person:
    def __init__(self): # 초기자(생성자 함수) self 구문은 내재화된 구문 텍스트이다.
        self.name = "강하늘"
        self.age = 30


p = Person() #객체변수 - 인스턴스화 되었다. 메모리에 로드되었다.
print(p.name)
print(p.age)
print(p.name, p.age)