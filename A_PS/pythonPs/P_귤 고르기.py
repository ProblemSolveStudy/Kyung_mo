tangerine = 	[1, 3, 2, 5, 4, 5, 2, 3]
answer = 0
a = {}
for i in tangerine:
    if i in a:
        a[i] += 1
    else:
        a[i] = 1

a = dict(sorted(a.items(), key = lambda x: x[1], reverse=True))
print(a)

for i in a:
    print("a 의 키값" + str(a[i]))
    print("a의 값" + str(i))