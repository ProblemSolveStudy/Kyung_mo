import sys

# 각 레벨을 클리어할 때 주는 점수가 증가하게 만들어야 한다.
# 몇 번 감소시키면 되는지 구하는 프로그램을 작성해라.
# 1만큼 감소시키는 것이 1번이다.
# 점수 내리는 것을 최소화 해야 한다.

n = int(sys.stdin.readline())
score = [int(sys.stdin.readline()) for _ in range(n)]

answer = 0

for i in range(len(score)-2, -1, -1):
    if score[i] >= score[i+1]:
        answer += score[i] - score[i+1] + 1
        score[i] = score[i+1] - 1

print(answer)