def solution(picks, minerals):
    minerals = [list(minerals[i:i+5]) for i in range(0, min(sum(picks)*5, len(minerals)), 5)]
    costs = []
    for mineral in minerals:
        cost = [0,0,0]
        for mine in mineral:
                if mine == 'diamond':
                    cost[0] += 1
                    cost[1] += 5
                    cost[2] += 25
                elif mine == 'iron':
                    cost[0] += 1
                    cost[1] += 1
                    cost[2] += 5
                else:
                    cost[0] += 1
                    cost[1] += 1
                    cost[2] += 1
        costs.append(cost)

    costs.sort(key=lambda x:(-x[2],-x[1]))

    ans = 0
    for score in costs:
        if picks[0]:
            ans += score[0]
            picks[0] -= 1
        elif picks[1]:
            ans += score[1]
            picks[1] -=1
        elif picks[2]:
            ans += score[2]
            picks[2] -= 1
        else:
            break
    
    return ans

print(solution(picks=[1, 3, 2], minerals=["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))