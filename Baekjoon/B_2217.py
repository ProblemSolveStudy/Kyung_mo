import sys
n = int(sys.stdin.readline())
rope = []
for i in range(n):
    rope.append(int(sys.stdin.readline()))

rope.sort(reverse=True)
result = []
for i in range(len(rope)):
    result.append(rope[i] * (i+1))

print(max(result))