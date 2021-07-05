with open('scores.txt', 'a') as f:
    name = input("이름 입력 : ")
    kor = int(input("국어 점수 : "))
    math = int(input("수학 점수 : "))
    avg = (kor + math) / 2

    key = " "
    key = input('성적을 저장할까요(y/n)? : ')

try:
    if key == 'y' or key == 'Y':
        with open('scorelist.txt', 'a') as f:
            f.write(name + ' ')
            f.write(str(kor) + ' ')
            f.write(str(math) + ' ')
            f.write(str(avg) + '\n')

    elif key == 'n' or key == 'N':
        break

    else:
        print("잘못된 입력입니다. 다시 선택하세요.")


except ValueError:
    print("잘못된 입력입니다. 다시 선택하세요.")



