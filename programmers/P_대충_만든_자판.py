def solution(keymap, targets):
    answer = []
    dict_arr = []
    for key in keymap:
        hashmap = dict()
        for i, val in enumerate(key):
            if val not in hashmap:
                hashmap[val] = i
        dict_arr.append(hashmap)

    new_hashmap = dict()
    
    for dict_item in dict_arr:
        for key, value in dict_item.items():
            if key in new_hashmap:
                new_hashmap[key] = min(value, new_hashmap[key])
            else:
                new_hashmap[key] = value
    for target in targets:
        cnt = 0
        for t in target:
            if t in new_hashmap:
                cnt += new_hashmap[t] + 1
            else:
                cnt = -1
                break
        answer.append(cnt)
    return answer