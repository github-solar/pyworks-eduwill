#Student class - 정보은닉

class Student:
    def __init__(self, sid, name):
        self.sid = "1001"
        self.name = "강하늘"



s1 = Student(1002, "김바다")

print(s1.sid, s1.name)


# 위의 알고리즘은 정보보안이 안된 상태