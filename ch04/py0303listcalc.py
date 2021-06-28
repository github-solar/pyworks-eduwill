# list 연산

score = [79, 80, 50, 60, 90, 45]
sum=0
avg =0.0
count = len(score) # len 리스트 요소의 갯수 구하는 함수

# 합계
for i in score:
    sum +=i
    print("i=%d, sum=%d" % (i, sum))

# 평균
avg = sum / count

print("개수 : %d개" % count)
print("합계 : %d점" % sum)
print("평균 : %.1f점" % avg) # 소수점이하 첫째자리까지 표시하라.
