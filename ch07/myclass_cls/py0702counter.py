#counter 클래스

class Counter:
    def __init__(self):
        self.x = 0 #인스턴스 변수 (메모리의 힙영역에 로드된다. 매번 초기화된다.)
        self.x = self.x + 1

    def showinfo(self):
        print(self.x)


c1 = Counter()
c1.showinfo()
c2 = Counter()
c2.showinfo()
c3 = Counter()
c3.showinfo()