import sys
word = sys.stdin.readline().rstrip()
for i in range(0,len(word), 10):
    print(word[i:i+10])