def solution(babbling):
    answer = 0
    pron = ["aya", "ye", "woo", "ma"]
    
    for i in babbling:
        for p in pron:
            if p * 2 not in i:
                i = i.replace(p, ' ')
        i=i.replace(' ', '')
        if len(i) == 0:
            answer += 1
    return answer

solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])