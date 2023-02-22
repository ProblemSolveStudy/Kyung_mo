# 중첩 덧셈연산
# 빨리끝나는 사람 순으로 세우는 것이 최소값
# 40ms
# O(n log n)
import sys

n = int(sys.stdin.readline())

time = list(map(int, sys.stdin.readline().rstrip().split()))

time.sort() 

result = 0
acc_result = 0

# O(n)
for i in time:
    acc_result += i
    result += acc_result

print(result)


# 슬라이싱 이용한 풀이방법
# 48ms
# 그러면 O(nlogn)이랑 O(n) 같이 있으니까 더 큰 O(nlogn)이 복잡도인가?

# for i in range(1, n+1):
#     result += sum(time[:i])
# print(result)

# 슬라이싱을 이용한 풀이방법과 누적합으로 구하는 방법으로 진행함
# 슬라이싱을 이용한 방법이 8ms 더 느렸음. 슬라이싱은 index로 list를 돌아다녀야 해서 느려지는 것인가??????????????




# 이중포문
# 88ms
# O(n^2)
# import sys

# N = int(sys.stdin.readline())

# time = list(map(int, sys.stdin.readline().rstrip().split()))
# result = 0
# time.sort()

# for i in range(N):
#     for j in range(i+1):
#         result += time[j]

# print(result)