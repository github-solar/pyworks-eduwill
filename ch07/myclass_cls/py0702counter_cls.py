#counter 클래스 호출하여 연산에 활용

class Counter:
    x = 0
    def __init__(self):

        Counter.x += 1

    def showinfo(self):
        print(self.x)


c1 = Counter()
c1.showinfo()
c2 = Counter()
c2.showinfo()
c3 = Counter()
c3.showinfo()