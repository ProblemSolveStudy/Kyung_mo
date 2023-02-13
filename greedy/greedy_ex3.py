import sys

n = int(sys.stdin.readline())
adv = list(map(int, sys.stdin.readline().rstrip().split()))

adv.sort()

result = 0
count =0 

for i in adv:
    count += 1
    if count >= i:
        result += 1
        count =0

print(result)