import sys

arr = [int(sys.stdin.readline()) for _ in range(5)]

arr.sort()

avg = sum(arr) // 5

print(avg)

if len(arr) % 2 == 0:
    middle = (arr[len(arr) // 2] + arr[len(arr) // 2 + 1]) // 2
else:
    middle = len(arr) // 2

print(arr[middle])