# 일단 주어지는 입력의 수가 1천만이다.
# 게다가 시간제한은 1초기 때문에 O(n)이하의 시간복잡도로 문제를 풀어야 한다.
import sys

N = int(sys.stdin.readline())
n_arr = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().split()))

cnt = {}
for card in n_arr:
    if card in cnt:
        cnt[card] += 1
    else:
        cnt[card] = 1

def binary_search(arr, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if arr[mid] == target:
        return cnt.get(target)
    if arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)

for target in m_arr:
    print(binary_search(n_arr, target, 0, N-1), end=' ')