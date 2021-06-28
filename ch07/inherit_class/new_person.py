# 멤버 매개변수가 있는 상속 유형

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age



class Employee(Person):
    def __init__(self, name, age, empid):
        super().__init__(name, age) # 부모클래스의 사전정의 매개변수 2개를 가져오는 구문
        self.empid = empid          # super() 함수(또는 객체)를 선언해야 한다.
                                    # 자기자신 것은 self.변수명

e1 = Employee("남한산성", 20, 201)
print(e1.name, e1.age, e1.empid)

e2 = Employee("북한산", 25, 202)
print(e2.name, e2.age, e2.empid)

