import sys

n = int(sys.stdin.readline())
target = 1000 - n
arr = [500, 100, 50,10, 5, 1]
cnt = 0
for i in arr:
    cnt += target//i
    target %= i
print(cnt)