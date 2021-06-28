#장바구니 클래스

class Cart:

    li = []

    def __init__(self, goods):
        Cart.li.append(goods) # 클래스 명칭을 직접 호출한다.

    def showinfo(self):
        print(self.li)

c1 = Cart('커피')
c1.showinfo()
c2 = Cart('달달')
c2.showinfo()
c3 = Cart('양파')
c3.showinfo()