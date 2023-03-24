import sys

_ = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().rstrip().split()))
n_arr.sort()
_ = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().rstrip().split()))

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return array[start:end+1].count(array[mid])
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

dic = {}
for i in n_arr:
    if i not in dic:
        dic[i] = binary_search(n_arr, i, 0, len(n_arr)-1)
print(' '.join(str(dic[x]) if x in dic else '0' for x in m_arr))