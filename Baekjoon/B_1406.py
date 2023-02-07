import sys

rightStack = []
leftStack = list(sys.stdin.readline().rstrip()) # abcd 들어옴

t = int(input())

for i in range(t):
    com = sys.stdin.readline().split()

    if com[0] == 'L':
        if leftStack:
            rightStack.append(leftStack.pop())
    elif com[0] == 'D':
        if rightStack:
            leftStack.append(rightStack.pop())
    elif com[0] == 'B':
        if leftStack:
            leftStack.pop()
    elif com[0] == 'P':
        leftStack.append(com[1])

rightStack.reverse()

for i in leftStack + rightStack:
    print(i, end='')