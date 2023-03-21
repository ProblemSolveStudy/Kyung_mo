# 퀵정렬은 피벗을 설정해놓고 진행해줘야 한다
# 왼쪽에서는 피벗보다 큰 데이터를 선택해주고, 오른쪽에서는 피벗보다 작은 데이터를 선택해준다.
# 왼쪽과 오른쪽의 위치가 엇갈리게 되면 '피벗'과 '피벗보다 작은 데이터'의 위치를 변경한다

# 퀵 정렬의 시간복잡도 O(NlogN)
# 최악의 경우 O(n^2)

array = [5, 7, 9, 0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start>=end:
        return
    
    pivot = start # 피벗은 첫번째 원소
    left = start+1
    right = end
    while (left <= right):
        while (left <= end and array[left] <= array[pivot]):
            left += 1
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if (left > right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)