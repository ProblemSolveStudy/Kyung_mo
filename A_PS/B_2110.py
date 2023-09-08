import sys
n,c = map(int, sys.stdin.readline().split())
graph = [int(sys.stdin.readline()) for _ in range(n)]

graph.sort()

start = min(graph)
end = max(graph)
result = 0
while start <= end:
    mid = (start + end) // 2
    total = 1
    old = graph[0]
    for i in range(1, len(graph)):
        if graph[i] >= old + mid:
            total += 1
            old = graph[i]
    
    if total >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)