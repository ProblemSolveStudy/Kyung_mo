import sys

n = int(sys.stdin.readline())
tower = list(map(int,sys.stdin.readline().rstrip().split()))
stack = []
res = [0] * n

for i in range(n):
    if not stack:
        stack.append([tower[i], i])
        res[i] = 0
    else:
        while True:
            if stack[-1][0] >= tower[i]:
                res[i] = stack[-1][1] + 1
                stack.append([tower[i], i])
                break
            else:
                stack.pop()
            
            if not stack:
                stack.append([tower[i], i])
                break
                
print(*res)