import sys

# 우선 입력값이 최대 100_000 이기 때문에 O(n^2) 을 넘어가면 안되기 때문에 그리디
# 모두 점수가 높은 애를 전체에서 뺀다?

t = int(sys.stdin.readline())

# man2= [[3,6],[7,3],[4,2],[1,4],[5,7],[2,5],[6,1]]

# manSum = [5,5,5,5,10]
# manSum.sort()


# for i in range(t):
#     man = []
#     n = int(sys.stdin.readline())
#     result = 1
#     for j in range(n):
#         score = list(map(int, sys.stdin.readline().split()))
#         man.append(score)
    
    
#     man.sort(key=lambda x: x[0])

#     target = man[0][1]
#     for k in range(1, n):
#         if target > man[k][1]:
#             result += 1
#             target = man[k][1]


#     print(result)
    
    

# man.sort(key=lambda x:(x[0], x[1]))
# [[1, 4], [2, 3], [3, 2], [4, 1], [5, 5]]

# man2.sort(reverse=True, key=lambda x:(x[0], x[1]))
# [[7, 3], [6, 1], [5, 7], [4, 2], [3, 6], [2, 5], [1, 4]]
# 10        7       12      6       9       7       5


# for i in range(t):
#     app =[]
#     n = int(sys.stdin.readline())
#     cnt=1
#     for j in range(n):
#         app.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
#     app.sort()

#     target=app[0][1]

#     for k in range(1,n):
#         if target > app[k][1]:
#             cnt+=1
#             target = app[k][1]
    
#     print(cnt)

for i in range(t):
    n = int(sys.stdin.readline())
    app=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    app.sort(key=lambda x:x[0])
    cnt=1
    target = app[0][1]

    for k in range(1, n):
        if target > app[k][1]:
            cnt += 1
            target = app[k][1]

    print(cnt)
