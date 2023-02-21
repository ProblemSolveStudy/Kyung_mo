import sys
input = sys.stdin.readline


guitar, brand = map(int,input().split())


pakageBrands = [list(map(int, input().split())) for _ in range(brand)]
singleBrands = pakageBrands.copy()

pakageBrands.sort(key=lambda x:(x[0]))
singleBrands.sort(key=lambda x:x[1])

pakageMinCost = pakageBrands[0][0]
singleMinCost = singleBrands[0][1]

result = 0

while True:
    temp = guitar // 6
    if guitar <= 6:
        minCost = min(pakageMinCost, singleMinCost * guitar)
        result += minCost
        break
    minCost = min(pakageMinCost, singleMinCost * 6)
    result += temp * minCost
    guitar -= temp * 6
    
print(result)