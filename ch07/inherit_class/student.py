from person import Person
#Student class - 부모 클래스 상속하여 학번을 추가

class Student(Person):
    def __init__(self, name, age, stuid):
        super().__init__(name, age)
        self.stuid = stuid

    def showinfo(self):
        print(self.name, self.age, self.stuid)
s1 = Student("이바다", 19, 101)
s1.showinfo()