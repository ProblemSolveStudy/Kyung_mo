def solution(number, k):
    answer = []
    number = list(number)
    stack = [number.pop(0)]
    for num in number:
        if stack[-1] >= num:
            stack.append(num)
        elif stack[-1] < num:
            while stack and stack[-1] < num and k > 0:
                stack.pop()
                k -= 1
            stack.append(num)
            
    if k:
        stack = stack[:-k]
    answer = ''.join(stack)
    return answer