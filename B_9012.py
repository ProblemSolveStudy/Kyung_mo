import sys

t = int(sys.stdin.readline())
for _ in range(t):
    test = sys.stdin.readline()
    stack = []
    for i in test:
        if i == '(':
            stack.append('(')

        elif i==')':
            if len(stack) == 0:
                stack.append(')')
                break;
            else:
                stack.pop()

    if len(stack) == 0:
        print("YES")
    else:
        print("NO")