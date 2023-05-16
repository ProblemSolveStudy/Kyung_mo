park = ["OSO","OOO","OXO","OOO"]

routes = ["E 2","S 3","W 1"]

def solution(park, routes):
    graph = []

    for i in park:
        graph.append(list(i))

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 'S':
                x = i
                y = j
    # 상하좌우
    for route in routes:
        nx,ny = x, y

        if route[0] == 'E':
            for _ in range(int(route[2])):
                if ny+1 >= len(park[0]) or park[x][ny+1] == 'X':
                    ny = y
                    break
                else:
                    ny += 1
            y = ny

        elif route[0] == 'W':
            for _ in range(int(route[2])):
                if ny -1 < 0 or park[x][ny-1] == 'X':
                    ny = y
                    break
                else:
                    ny -= 1
            y = ny

        elif route[0] == 'S':
            for _ in range(int(route[2])):
                if nx+1 >= len(park) or park[nx+1][y] == 'X':
                    nx = x
                    break
                else:
                    nx += 1
            x = nx
        elif route[0] == 'N':
            for _ in range(int(route[2])):
                if nx-1 < 0 or park[nx-1][y] == 'X':
                    nx = x
                    break
                else:
                    nx -= 1
            x = nx
    return [x,y]


print(solution(park, routes))