#04일05 함수_사용자 정의 함수


#return 이 없고 매개변수 없는 함수
def say_hello():
    print("hello")


say_hello() #함수 호출

print('='*50)

#return 없고, 매개변수 있는 함수
def say_hello2(name):
    print(name, "님 반갑습니다.")
    print("{}님 반갑습니다.".format(name))

say_hello2('김대한')

print('='*50)


    
    
