from urllib import request
from bs4 import BeautifulSoup

html = request.urlopen("https://finance.naver.com/marketindex/")
code = html.read().decode('euc-kr', 'replace').encode('utf-8', 'replace') # 글자 깨짐 방지 구문
contents = BeautifulSoup(code, 'html.parser')
lis = contents.select("ul.data_lst li") #리스트로 반환받자
#lis = ul.find_all('li')

for li in lis:
    ex = li.select_one("span.blind") #환율 종류
    val = li.select_one("span.value") #환율 지수
    print(ex.string.split(' ')[-1], ':', val.string)
    #print(val.string)

