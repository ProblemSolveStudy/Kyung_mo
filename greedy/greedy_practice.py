n = 3020
cnt = 0

arr = [500, 100, 50, 10]

for coin in arr:
    cnt += n // coin
    n %= coin
print(cnt)