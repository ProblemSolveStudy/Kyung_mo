from collections import deque
def is_bracket(s):
    stack = []
    
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
        
    if len(stack) == 0:
        return True
    else:
        return False
    
def solution(s):
    answer = 0
    s = deque(s)
    
    for i in range(len(s)):
        if is_bracket(s): answer += 1
        s.rotate(-1)
    return answer