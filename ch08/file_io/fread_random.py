# 구단을 1개씩 랜덤 추출
import random

try:
    f = open('e:/python/pyworks-jds/pyfile/2021kbo.txt', 'r')
    data = f.read().split() #splite()가 없을 때는 어떻게 출력되는가 구별
    #splite()는 자료를 공백으로 구분한다.
    team = random.choice(data)
    print(team)

    f.close()

except FileNotFoundError as e:
    print(e)