numbers = [2, 3, 3, 5]
stack = []
answer = [-1] * len(numbers)

for i in range(len(numbers)):
    while stack and numbers[stack[-1]] < numbers[i]:
        answer[stack.pop()] = numbers[i]
    stack.append(i)