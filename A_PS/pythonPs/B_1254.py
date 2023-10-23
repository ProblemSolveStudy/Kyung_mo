import sys
word = sys.stdin.readline().rstrip()

for i in range(len(word)):
    if word[i:] == word[i:][::-1]:
        pal = word + word[:i][::-1]
        print(len(pal))
        break