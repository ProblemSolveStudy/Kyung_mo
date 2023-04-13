# 탑다운
d = [0] * 100

def fibo(x):
    print('f(' + str(x) + ')', end=' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

fibo(6)

# 보텀업

# d[1] = 1
# d[2] = 1
# n = 99

# for i in range(3, n + 1):
#     d[i] = d[i - 1] + d[i - 2]

# print(d[n])