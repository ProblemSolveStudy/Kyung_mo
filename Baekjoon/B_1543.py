# import sys

# doc = sys.stdin.readline().rstrip()
# word = sys.stdin.readline().rstrip()

# cnt = 0
# i = 0
# while i <= len(doc) - len(word):
#     if doc[i:i+len(word)] == word:
#         cnt+=1
#         i += len(word)
#     else:
#         i += 1

# print(cnt)

import sys

docs = sys.stdin.readline().rstrip()
word = sys.stdin.readline().rstrip()

cnt = 0
i = 0
while i<= len(docs) - len(word):
    if docs[i:i+len(word)] == word:
        cnt += 1
        i += len(word)
    else:
        i += 1
print(cnt)