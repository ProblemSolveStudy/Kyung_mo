from collections import deque
def solution(cards1, cards2, goal):
    answer = ''
    result = []
    cards1, cards2 = deque(cards1), deque(cards2)
    for i in range(len(goal)):
        tmp = goal[i]
        
        if tmp in cards1:
            if cards1[0] == tmp:
                result.append(cards1.popleft())
        elif tmp in cards2:
            if cards2[0] == tmp:
                result.append(cards2.popleft())
    
    if result == goal:
        answer = "Yes"
    else:
        answer = "No"
    return answer

print(solution(["i", "water", "drink"],	["want", "to"],	["i", "want", "to", "drink", "water"]))