# Person클래스, 멤버변수(name, age) 부모역할
# Employee 클래스는 Person 클래스를 상속한다.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    pass

if __name__ == "__main__":
    p1 = Person('한강', 25)
    print(p1.name, p1.age)

    e1 = Employee('남한강', 30)
    print(e1.name, e1.age)

    e2 = Employee('북한강', 34)
    print(e2.name, e2.age)



