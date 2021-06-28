# 이것은 하나의 클래스에 복수의 객체를 저장하는 형식이다.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("박대양", 40)
print(p1.name, p1.age)
p2 = Person("이선", 33)
print(p2.name, p2.age)

