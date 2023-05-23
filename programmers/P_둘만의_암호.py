s = "zzzzz"
skip = "a"
index = 1

def solution(s, skip, index):
    answer = []
    s_list = list(s)
    for word in s_list:
        new_word = chr(ord(word) + index)
        
        cnt = 0
        for i in range(ord(word), ord(new_word) + 1):
            if chr(i) in skip:
                cnt += 1
        
        new_word = chr(ord(word) + index + cnt)
        if ord(new_word) >= 123:
            new_word = chr(ord(new_word) - 26)
            for i in new_word:
                if i in skip:
                    cnt += 1
            
        answer.append(chr(ord(new_word) + cnt))
        
    for n in answer:
        print(n, end='')

solution(s, skip, index)