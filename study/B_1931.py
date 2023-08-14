import sys
input = sys.stdin.readline

n = int(input())
room = [list(map(int, input().rstrip().split())) for _ in range(n)]

room.sort(key=lambda x:(x[1], x[0]))
cnt = 0

for i in room:
    if cnt == 0 or i[0] >= finish:
        cnt+=1
        finish = i[1]

print(cnt)