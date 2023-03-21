array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # i부터 1까지 1씩 감소하는 문법
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)

#시간 복잡도 O(n^2)
# 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 O(n)