# 1. 콘센트 개수만큼 데이터를 넣는다.
# 2. 콘센트가 비어있으면 순서대로 넣는다.
# 3. 콘센트 개수 이후부터는 내가 쓰
#     3-1. 있다면, 패스한다
#     3=2. 없다면, cnt += 1


import sys

input = sys.stdin.readline

n, k = map(int, input().split())

arr = list(map(int, input().split()))

socket = []

cnt =0

for i in arr:
    # 멀티탭에 빈자리가 있을 땐 값을 넣어줌
    if len(socket) < n:
        socket.append(i)
    elif i in socket:
        pass
    else:
        for j in socket:
            if j not in arr[arr.index(i):]:
                tmp = j

print(cnt)