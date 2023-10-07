from collections import deque
def is_bracket(s):
    stack = []
    for bracket in s:
        if len(stack) == 0: stack.append(bracket)
        else:
            if bracket == ']' and stack[-1] == '[':
                stack.pop()
            elif bracket == ')' and stack[-1] == '(':
                stack.pop()
            elif bracket == '}' and stack[-1] == '{':
                stack.pop()
            else: stack.append(bracket)
    return 1 if len(stack) == 0 else 0

def solution(s):
    answer = 0
    s = deque(s)
    for i in range(len(s)): # 5번 회전
        if is_bracket(s): answer += 1
        s.rotate(-1)
    return answer

solution("}]()[{")