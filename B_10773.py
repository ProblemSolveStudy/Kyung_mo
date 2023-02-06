import sys

left = list(sys.stdin.readline().rstrip())

right = []

m = int(input())

for i in range(m):
    com = sys.stdin.readline().split()

    if com[0] == 'L':
        if left:
            right.append(left.pop())
    elif com[0] == 'D':
        if right:
            left.append(right.pop())
    elif com[0] == 'B':
        if left:
            left.pop()
    elif com[0] == 'P':
        left.append(com[1])

right.reverse()
for i in left+right:
    print(i, end='')
