import sys

args = sys.argv[1:]
#print(args)
sum = 0

for i in args:
    sum = sum + int(i)

print(sum)

