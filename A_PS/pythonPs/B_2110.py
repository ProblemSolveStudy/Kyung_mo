import sys
n,c = map(int, sys.stdin.readline().split())
graph = [int(sys.stdin.readline()) for _ in range(n)]

start = 1
end = max(graph)
graph.sort()
result = 0

while start <= end:
    total = 1
    mid = (start + end) // 2
    old = graph[0]
    for i in range(1, len(graph)):
        if graph[i] >= old + mid:
            total += 1
            old = graph[i]
    if total < c:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)