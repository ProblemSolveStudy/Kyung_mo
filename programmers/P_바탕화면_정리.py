def solution(wallpaper):
    INF = 10e9
    answer = []
    graph = []
    top, left, bottom, right = INF, INF, -INF, -INF
    
    for i in wallpaper:
        graph.append(list(i))
    
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == '#':
                top = min(top, i)
                left = min(left, j)
                bottom = max(bottom, i+1)
                right = max(right, j+1)
        
    print(top, left, bottom, right)
                
    return answer

wallpaper = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]
solution(wallpaper)