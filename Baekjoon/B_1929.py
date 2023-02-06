m, n = map(int, input().split())

arr = [0 for i in range(n+1)]

for i in range(2, n+1):
    arr[i] = i

for i in range(2, n+1):
    if arr[i] == 0: continue
    for j in range(i+i, n+1, i):
        arr[j] = 0

for i in range(m, n+1):
    if arr[i] != 0: print(arr[i])