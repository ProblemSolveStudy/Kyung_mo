import sys
arr = list(sys.stdin.readline().rstrip())
arr.sort(reverse=True)
result = "".join(arr)
print(result)