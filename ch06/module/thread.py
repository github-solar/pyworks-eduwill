#threading 모듈

import threading

def function_a(): #콜백함수 생성
    print('5초 간격으로 실행')
    timer = threading.Timer(5, function_a) #함수가 자기 자신을 호출 (=재귀호출) 할 때는 ()를 반드시 뺀다.
    timer.start()

function_a()
