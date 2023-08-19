import sys
n,m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    card.sort()
    result = card[0] + card[1]
    card[0], card[1] = result, result

print(sum(card))