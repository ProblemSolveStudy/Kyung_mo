# import sys
# from collections import Counter

# input = sys.stdin.readline

# n,m = map(int, input().split())

# dna = [list(input().rstrip()) for _ in range(n)]
# newDNA = ''
# result = 0
# for i in range(m):
#     a, c, g, t = 0, 0, 0 , 0
#     for j in range(n):
#         if dna[j][i] == 'A':
#             a += 1
#         elif dna[j][i] == 'C':
#             c += 1
#         elif dna[j][i] == 'G':
#             g += 1
#         elif dna[j][i] == 'T':
#             t += 1
    
#     if max(a,c,g,t) == a:
#         newDNA += "A"
#         result += c+g+t
#     elif max(a,c,g,t) == c:
#         newDNA += "C"
#         result += a+g+t
#     elif max(a,c,g,t) == g:
#         newDNA += "G"
#         result += c+a+t
#     elif max(a,c,g,t) == t:
#         newDNA += "T"
#         result += c+g+a

# print(newDNA)
# print(result)

import sys
input = sys.stdin.readline
n,m = map(int, input().split())

dna = [list(input().rstrip())for _ in range(n)]
newDna = ""
# print(dna)

result = 0
for i in range(m):
    a,c,g,t = 0,0,0,0
    for j in range(n):
        if dna[j][i] == 'A':
            a+=1
            
        elif dna[j][i] == 'C':
            c+=1
            
        elif dna[j][i] == 'G':
            g+=1
            
        elif dna[j][i] == 'T':
            t+=1
            
    
    if max(a,c,g,t) == a:
        newDna+='A'
        result += t+c+g
    elif max(a,c,g,t) == c:
        newDna+='C'
        result += a+t+g
    elif max(a,c,g,t) == g:
        newDna+='G'
        result += a+c+t
    elif max(a,c,g,t) == t:
        newDna+='T'
        result += a+c+g

print(newDna)
print(result)