import sys
input = sys.stdin.readline

N = int(input())
n_arr = sorted(list(map(int, input().split())))
M = int(input())
m_arr = list(map(int, input().split()))

def binary_search(arr, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if arr[mid] == target:
        return True
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)

for target in m_arr:
    result = binary_search(n_arr, target, 0, N-1)
    if result:
        print(1)
    else:
        print(0)
