# 최대한 빨리 끝나는 회의가 많을 수록 많은 경우의수가 생김

import sys

n = int(sys.stdin.readline()) # 회의의 수
mr = []

# 각 회의의 정보를 입력과 동시에 list에 넣어줌
# [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]
for _ in range(n):
    mr.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 가장 먼저 끝나는 회의순으로 mr list를 정렬함
# [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]
mr.sort(key=lambda x: (x[1], x[0]))

# 최대 개수 cnt
cnt = 0

# mr list에 내용물을 i로 ex) i=0 [1,4]; i=1 [3,5] 출력됨 
for i in mr:
    # 가장 먼저 첫 값의 cnt를 올려주기 위해 cnt == 0 조건 추가
    if cnt == 0 or i[0] >= finish:
        cnt += 1
        finish = i[1]

print(cnt)