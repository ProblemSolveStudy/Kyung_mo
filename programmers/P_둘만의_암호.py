s = "aukks"
skip = "wbqd"
index = 5
def solution(s, skip, index):
    answer = ''
    skip = set(ord(w) for w in skip)
    for word in s:
        cnt = index
        word = ord(word)
        while cnt != 0:
            word += 1
            if word > ord('z'):
                word = word - ord('z') + ord('a') - 1
            if word in skip:
                continue
            cnt -= 1
        answer += chr(word)
    return answer
    
    # for i in s:
    #     i = chr(ord(i) + index)
    #     if ord(i) + index > ord("z"):
    #         i = chr(ord(i) + index - 26)
        
    #     if i in skip:
    #         i = chr(ord(i) + 1)
    #     answer.append(i)
    
    # return answer
print(solution(s, skip, index))