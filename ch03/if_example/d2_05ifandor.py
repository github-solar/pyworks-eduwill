#이론: if문에서 논리식의 조건이 2이상인 경우
#조건 : 현금, 카드 있으면 택시를 타고 아니면 걸어간다.

money = 3000
card = True

if money > 4000 or not card:
    print("택시")
else:
    print("뚜벅")


pocket = ['paper','스마트폰','money']
if 'money' in pocket:
    print('택시')
else:
    print('뚜벅')
    
    
    
