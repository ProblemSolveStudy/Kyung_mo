import sys
sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

# 선택정렬
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i+1, len(arr)):
#         if arr[min_index] > arr[j]:
#             min_index = j
#     arr[i], arr[min_index] = arr[min_index] , arr[i]

# 삽입정렬
# for i in range(1, len(arr)):
#     for j in range(i, 0, -1):
#         if arr[j] < arr[j-1]:
#             arr[j], arr[j-1] = arr[j-1], arr[j]
#         else:
#             break

# def quick_sort(array, start, end):
#     if start >= end:
#         return
    
#     pivot = start
#     left = start+1
#     right = end
#     while (left <= right):
#         while (left <= end and array[left] <= array[pivot]):
#             left += 1
#         while (right > start and array[right] >= array[pivot]):
#             right -= 1
#         if left > right:
#             array[right], array[pivot] = array[pivot], array[right]
#         else:
#             array[left], array[right] = array[right], array[left]
#     quick_sort(array, start, right - 1)
#     quick_sort(array, right + 1, end)

# quick_sort(arr, 0, len(arr) - 1)

arr.sort()

for i in range(len(arr)):
    print(arr[i])