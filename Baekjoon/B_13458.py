import sys
input = sys.stdin.readline

n = int(input())
room = list(map(int, input().rstrip().split()))


b, c = map(int, input().split())

cnt = n
for i in room:
    i -= b
    if i>0:
        if i % c:
            cnt += (i // c) + 1
        else:
            cnt += (i//c)

print(cnt)