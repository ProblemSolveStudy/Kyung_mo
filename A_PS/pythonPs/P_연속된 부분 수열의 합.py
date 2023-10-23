def solution(sequence, k):
    answer = []
    sum = 0
    start = 0
    end = -1

    while True:
        if sum < k:
            end += 1
            if end >= len(sequence):
                break
            sum += sequence[end]
        else:
            sum -= sequence[start]
            start += 1
            if start >= len(sequence):
                break
        if sum == k:
            answer.append([start, end])
    answer.sort(key=lambda x: (x[1] - x[0], x[0]))
    return answer[0]

sequence = [1, 1, 1, 2, 3, 4, 5]
k = 5
print(solution(sequence, k))
