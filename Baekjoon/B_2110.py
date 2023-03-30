import sys
input = sys.stdin.readline

n,c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

start = 0 # 집의 좌표는 0부터 시작한다
end = max(arr) # 집의 좌표중 가장 마지막 숫자

result = 0 # 값을 갱신해줄 변수
while (start<= end): # 최적의 해를 찾기 위한 조건
    current = arr[0]
    total = 1 # arr[0]을 잡고 시작한다는 마인드
    mid = (start+end)//2 # 중간값 잡아주고

    for i in range(1, len(arr)): # current 다음수부터 하나씩 검사한다
        if arr[i] >= current + mid: # current에서 mid값을 더한 값보다 크거나 같으면 total 증가
            total += 1
            current = arr[i] # current값 갱신해주고
    
    if total < c: # c보다 작으니 mid값을 줄여서 더 짧은범위를 탐색하게 할 것
        end = mid - 1
    else: # c보다 많이 찾았으니 result에 우선 mid값 넣고, 최적의 해를 찾기 위해서 start값 갱신
        # 최대 mid값
        result = mid
        start = mid + 1

print(result)

# import sys
# input = sys.stdin.readline

# n,c = map(int, input().split())
# arr = sorted([int(input()) for _ in range(n)])

# start = 0
# end = max(arr)

# while start <= end:
#     current = arr[0]
#     total = 1
#     mid = (start + end) // 2

#     for i in range(1, len(arr)):
#         if arr[i] >= current + mid:
#             total += 1
#             current = arr[i]
    
#     if total < c:
#         end = mid - 1
#     else:
#         result = mid
#         start = mid + 1
# print(result)