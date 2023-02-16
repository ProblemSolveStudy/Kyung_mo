import sys

# k개의 로프를 활용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 w/k만큼의 중량이다.

# 로프들을 이용해 들 수 있는 최대 중량 구하기

# n = int(sys.stdin.readline())
# rope = []
# for _ in range(n):
#     rope.append(int(sys.stdin.readline().rstrip()))

# rope.sort(reverse=True)
# result = []

# for i in range(n):
#     result.append(rope[i] * (i+1))

# print(max(result))

n = int(sys.stdin.readline())

rope = []
for i in range(n):
    rope.append(int(sys.stdin.readline().rstrip()))

rope.sort(reverse=True)
result = []

for i in range(n):
    result.append(rope[i] * (i+1))

print(max(result))