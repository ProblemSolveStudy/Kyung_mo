import sys
n, mileage = map(int, sys.stdin.readline().split())
cnt = 0

arr = []
for i in range(n): # O(n)
    app, max = map(int, sys.stdin.readline().split())
    subject = list(map(int, sys.stdin.readline().rstrip().split()))
    subject.sort() # O(nlogn)

    if app<=max:
        arr.append(1)
    else:
        idx = app - max
        arr.append(subject[idx])
arr.sort() # O(nlogn)
for i in arr: # O(n)
    mileage -= i
    if mileage < 0:
        break
    cnt += 1
print(cnt)