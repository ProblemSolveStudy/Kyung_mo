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

