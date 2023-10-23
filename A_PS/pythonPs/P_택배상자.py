answer = 0
support = [] # stack
order = [4,3,1,2,5]
i = 1
cnt = 0
while i != len(order) + 1:
    support.append(i)
    while support and support[-1] == order[cnt]:
        cnt += 1
        support.pop()
    i+=1