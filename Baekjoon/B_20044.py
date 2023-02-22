import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()
left = 0
right = len(arr)-1

minValue = 5000*100000
while left < right:
    tmp = arr[left] + arr[right]
    minValue = min(minValue, tmp)
    left += 1
    right -= 1

print(minValue)