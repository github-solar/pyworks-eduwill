'''
#1번 주어진 자연수가 홀수인지 짝수인지 판별 함수
def is_odd(number):
    if number % 2 != 0:
        return True
    else:
        return False

num = is_odd(11)
print(num)

#★★2번 가변매개변수
def avg_numbers(*args):
    result = 0
    for i in args:
        result +=i
        print(i,result) # 연산과정을 알고 싶으면 출력해봐라.
    return result / len(args)

print(avg_numbers(1,2))
print(avg_numbers(1,2,3,4,5))



#3 두 숫자 입력받아 더하여 반환

input1 = input('첫 번째 숫자를 입력하세요: ')
input2 = input('두번째 숫자를 입력하세요:')

total = int(input1) + int(input2)
print('두 수의 합은 %s 입니다.' % total)
# print('두 수의 합은 %s 입니다.' % total)


#4 다음 중 출력 결과가 다른 것은

print("you" "need" "python")
print("you"+"need"+"python")
print("you","need","python")
print("".join(["you","need","python"]))


#5
f1 = open('test.txt', 'w')
f1.write('Life is too short')
f1.close()

f2 = open('test.txt', 'r')

print(f2.read())
f2.close()


#6
user_input = input('저장할 내용을 입력하세요:')
f = open('test.txt', 'a')
f.write(user_input)
f.write('\n')
f.close()
'''

#7
f = open('test2.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f = open('test2.txt', 'w')
f.write(body)
f.close()


