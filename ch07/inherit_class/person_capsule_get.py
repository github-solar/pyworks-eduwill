# Person클래스, 멤버변수(name, age) 부모역할
# Employee 클래스는 Person 클래스를 상속한다.

class Person:
    def __init__(self, name, age): #여기서는 초기자를 설정한다.
        self.name = "강하늘"
        self.age = 30


p = Person() #객체변수 - 인스턴스화 된 후
p.name = "박바다"
print(p.name, p.age)



