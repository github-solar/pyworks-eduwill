#파썬01일연습01:변수값교환
blue = 1
red = 2

print('교환전 : ')
print('blue = ', blue, 'red = ', red)

print('교환후 : ')

#yellow 임시변수를 사용하여
yellow = blue
blue = red
red = yellow
print('blue = ', blue, 'red = ', red)
