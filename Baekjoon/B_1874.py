import sys

n = int(input())
leftStack = []
rightStack = []
start = 0
flag = True

for i in range(n):
    com = int(input())

    while start < com:
        start += 1
        leftStack.append(start)
        rightStack.append('+')

    if leftStack[-1] == com:
        leftStack.pop()
        rightStack.append('-')
    else:
        flag = False
        break

if flag == True:
    print('\n'.join(rightStack))
else:
    print("NO")