def solution(phone_book):
    answer = True
    
    # 이중 포문은 시간초과가 발생할거야
    
    phoneBook = sorted(phone_book)
    
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return answer

solution(["119", "97674223", "1195524421"])