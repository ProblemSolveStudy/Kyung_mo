def solution(players, callings):
    answer = []
    hashmap = dict()
    for i,val in enumerate(players):
        hashmap[val] = i
    for call in callings:
        pre, post = hashmap[call] - 1, hashmap[call]
        hashmap[players[pre]] = post
        hashmap[players[post]] = pre
        players[pre], players[post] = players[post], players[pre]
    answer = players
    return answer

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

print(solution(players, callings))