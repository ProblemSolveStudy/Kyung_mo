# 상근이가 몇개의 카드를 가지고 잇느냐! (비교대상의 카드들 중에서)
import sys
input = sys.stdin.readline

_ = int(input())
# 상근이꺼
n = sorted(list(map(int, input().split())))
_ = int(input())
# 비교대상
m = list(map(int, input().split()))

cnt = {}
for card in n:
    if card in cnt:
        cnt[card] += 1
    else:
        cnt[card] = 1

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start+end) // 2

        if arr[mid] == target:
            return cnt.get(target)
        if arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

# 비교대상의 카드들 중에서
for target in m:
    # 상근이의 카드들 n중 target(비교대상의 카드 한장)이 있나없나 찾기위해 이분탐색을 진행한다.
    print(binary_search(n, target, 0, len(n)-1), end=' ')