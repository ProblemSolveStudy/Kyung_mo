import sys

n = int(sys.stdin.readline())
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

lines.sort()

start = lines[0][0]
end = lines[0][1]
answer = 0

for i in range(1, n):
    if lines[i][0] <= end < lines[i][1]:
        end = max(end, lines[i][1])
    elif lines[i][0] > end:
        answer += end - start
        start = lines[i][0]
        end = lines[i][1]

answer += end - start
print(answer)