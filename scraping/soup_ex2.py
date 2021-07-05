# BeautifulSoup 모듈 사용하기
from bs4 import BeautifulSoup

html_str="""
<html>
<body>
    <ul class='item'>
        <li>인공지능</li>
        <li>빅데이터</li>
        <li>로봇</li>
    </ul>
    <ul class='lang'>
        <li>영어</li>
        <li>중국어</li>
        <li>한국어</li>
    </ul>
</body>
</html>
"""

contents = BeautifulSoup(html_str, 'html.parser')
ul = contents.find('ul', {'class':'lang'})
#print(ul)
#li = ul.find('li')
#print(li) #리스트의 맨위 요소만 검색된다.

#예제에서 중국어 검색하는 방법
lis = ul.find_all('li')
print(lis)
print(lis[1].text)


