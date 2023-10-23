def solution(clothes):
    answer = 0
    
    hash_map = dict()
    result = 1
    
    for wear, kind in clothes:
        hash_map[kind] = hash_map.get(kind,0) + 1
        
    for kind in hash_map:
        result *= (hash_map[kind] + 1)
    
    return result - 1

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])