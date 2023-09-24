import sys
n,m = map(int, sys.stdin.readline().split())
nli = list(sys.stdin.readline().rstrip() for _ in range(n))
nse = list(sys.stdin.readline().rstrip() for _ in range(m))

b3 = sorted(list(set(nli) & set(nse)))
print(len(b3), *b3, sep='\n')