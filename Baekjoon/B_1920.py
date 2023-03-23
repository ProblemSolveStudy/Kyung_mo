import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr.sort()
target_arr = list(map(int, sys.stdin.readline().split()))

# def binaray_search(array, target, start, end):
#     if start > end :
#         return None
#     mid = (start + end) // 2
#     if array[mid] == target:
#         return 1
#     elif array[mid] > target:
#         return binaray_search(array, target, start, mid-1)
#     else:
#         return binaray_search(array, target, mid+1, end)

# start = 0
# end = n-1
# for i in target_arr:
#     result = binaray_search(arr, i, start, end)
#     if result == None:
#         print(0)
#     else:
#         print(1)

def binaray_search(array, target, start, end):
    while start<=end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

for i in target_arr:
    result = binaray_search(arr, i, start=0, end=n-1)
    if result:
        print(1)
    else:
        print(0)