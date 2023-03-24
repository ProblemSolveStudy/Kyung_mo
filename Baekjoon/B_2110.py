import sys
from bisect import bisect_left, bisect_right

n,c = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]

