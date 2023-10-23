import sys
N = int(sys.stdin.readline())
cnt = N
for i in range(N):
    word = sys.stdin.readline()
    for j in range(0, len(word) - 1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break
print(cnt)