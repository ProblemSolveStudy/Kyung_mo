import sys

pipe = list(sys.stdin.readline().rstrip())
stack = []

cnt = 0
for i in range(len(pipe)):
    if pipe[i] == '(':
        stack.append('(')

    elif pipe[i] == ')':
        if pipe[i-1] == ')':
            stack.pop()
            cnt += 1
        elif pipe[i-1] == '(':
            stack.pop()
            cnt += len(stack)


print(cnt)