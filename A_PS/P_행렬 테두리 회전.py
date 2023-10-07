# def solution(rows, columns, queries):
#     answer = []
#     graph = []
#     for i in range(1, rows * columns + 1, columns):
#         graph.append([j for j in range(i, i + columns)])
        
#     for query in queries:
#         x1, y1, x2, y2 = query
#         tmp = graph[x1-1][y1-1]
#         minValue = tmp

#         for k in range(x1-1, x2-1):
#             graph[k][y1-1] = graph[k+1][y1-1]
#             minValue = min(minValue, graph[k][y1-1])

#         for k in range(y1-1, y2-1):
#             graph[x2-1][k] = graph[x2-1][k+1]
#             minValue = min(minValue, graph[x2-1][k])

#         for k in range(x2-1,x1-1,-1):
#             graph[k][y2-1] = graph[k-1][y2-1]
#             minValue = min (minValue, graph[k][y2-1])

#         for k in range(y2-1, y1-1, -1):
#             graph[x1-1][k] = graph[x1-1][k-1]
#             minValue = min(minValue, graph[x1-1][k])

#         graph[x1-1][y1] = tmp
#         answer.append(minValue)
#     return answer

def solution(rows, columns, queries):
    answer = []
    graph = [[0] * columns for _ in range(rows)]
    
    num = 1
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = num
            num += 1
    
    for query in queries:
        x1, y1, x2, y2 = query
        tmp = graph[x1-1][y1-1]
        minValue = tmp
        
        for k in range(x1-1, x2-1):
            graph[k][y1-1] = graph[k+1][y1-1]
            minValue = min(minValue, graph[k][y1-1])
            
        for k in range(y1-1, y2-1):
            graph[x2-1][k] = graph[x2-1][k+1]
            minValue = min(minValue, graph[x2-1][k])
        
        for k in range(x2-1, x1-1, -1):
            graph[k][y2-1] = graph[k-1][y2-1]
            minValue = min(minValue, graph[k][y2-1])
        
        for k in range(y2-1, y1-1, -1):
            graph[x1-1][k] = graph[x1-1][k-1]
            minValue = min(minValue, graph[x1-1][k])
        
        graph[x1-1][y1] = tmp
        answer.append(minValue)
    return answer

solution(6	,6,	[[2,2,5,4],[3,3,6,6],[5,1,6,3]])