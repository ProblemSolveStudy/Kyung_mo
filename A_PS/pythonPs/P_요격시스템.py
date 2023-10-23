targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]

result = 1
targets.sort(key=lambda x:x[1])

end = targets[0][1]

for i in range(1, len(targets)):
    if targets[i][0] >= end:
        result += 1
        end = targets[i][1]

print(result)