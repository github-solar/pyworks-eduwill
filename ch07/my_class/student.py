# 학생 클래스 생성과 사용

class Student:
    def __init__(self, sid, name):
        self.sid = sid #학번
        self.name = name

    def showinfo(self): # 간편하게 출력 메소드 생성
        print(self.sid, self.name)


if __name__ == "main":
    # 이렇게 선언하면 이 함수의 본래 파일에서만 실행되고,
    # import 된 다른 파일에서는 실행되지 않는다.
    s1 = Student(1001, "박대양")
    s1.showinfo()
    s2 = Student(1002, "이산")
    s2.showinfo()


