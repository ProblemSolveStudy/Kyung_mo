import sys
word = sys.stdin.readline().rstrip()
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in cro:
    word = word.replace(i, "a")
print(len(word))