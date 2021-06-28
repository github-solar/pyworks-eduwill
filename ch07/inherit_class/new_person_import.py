from person import Person
# 멤버 매개변수가 있는 상속 유형

'''
class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age        
        '''



class Employee(Person):
    def __init__(self, name, age, empid):
        super().__init__(name, age) # 부모클래스의 사전정의 매개변수 2개를 가져오는 구문
        self.empid = empid          # super() 함수(또는 객체)를 선언해야 한다.

    def getname(self): # 캡슐화(정보은닉) - get() 매서드 사용
        return self.name

    def getage(self):
        return self.age

    def getempid(self):
        return self.empid


e1 = Employee("남한산성", 20, 201)
print("이름 : ", e1.getname())
print("나이 : ", e1.getage())
print("사번 : ", e1.getempid())

e2 = Employee("북한산", 25, 202)
print(e2.name, e2.age, e2.empid)

# 위의 출력방식의 차이를 구별할 것.
