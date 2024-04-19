answer = []
list_x = []
list_y = []

for dot in [[1,1], [2,2], [1, 2]]:
    x, y = dot  # 현재 점의 x와 y 좌표를 추출
    if x not in list_x:
        list_x.append(x)
    if y not in list_y:
        list_y.append(y)

print(list_x + list_y)
