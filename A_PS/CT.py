answer = 0
elements = [7,9,1,1,4]
cycle = elements + elements
s = set()
for i in range(len(elements)):
    for j in range(len(elements)):
        s.add(sum(cycle[i:i+j]))