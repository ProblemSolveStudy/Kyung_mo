import sys

n = int(sys.stdin.readline())

time = list(map(int, sys.stdin.readline().rstrip().split()))

time.sort() # O(n log n)

result = 0
acc_result = 0

# O(n)
for i in time:
    acc_result += i
    result += acc_result

print(result)

# 슬라이싱 이용한 풀이방법

# for i in range(1, n+1):
#     result += sum(time[:i])
# print(result)

# 슬라이싱을 이용한 풀이방법과 누적합으로 구하는 방법으로 진행함
# 슬라이싱을 이용한 방법이 8ms 더 느렸음. 슬라이싱은 index로 list를 돌아다녀야 해서 느려지는 것인가??????????????

# 그러면 O(nlogn)이랑 O(n) 같이 있으니까 더 큰 O(nlogn)이 복잡도인가?