import sys
input = sys.stdin.readline

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
candidate = list(map(int, input().split()))

cnt = {}
for card in cards:
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
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)

for target in candidate:
    print(binary_search(cards, target, 0, N-1), end=' ')