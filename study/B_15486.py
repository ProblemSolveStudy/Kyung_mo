# 1. T 걸리는 시간, P 받는 금액
# 2. 최대 금액을 받을 수 있도록 하자!
# 3. N일 동안 최대한 많은 상담을 진행하도록 할 것이며 , 그러면서 최대 금액을 받아야 한다.
# 4. 최대 상담일자가 N일을 넘어가면 안된다.
# 5. 각 날짜를 할것인지 말것인지를 정해야 할듯함
# arr [[a,b]] a : 날짜 b: 금액

#     1. 만약 첫째날 일한다면?		 = 45 				
# 일				    1	2		3		4	    5	 6		7
# arr[i][0](상담일자)   3	5		1		1	    2	 4		2
# arr[i][1](상담 일자) 10	20		10	    20	    15	 40		200
# money(누적 돈)        0	0	    10	    30	    30	 45		45
# 가능한 금액	        0	0	  0,10,10   20, 30		        20, 45 	
# 											이거 두개는 일할 수가 없는 상태임	
							
							
# 	2. 만약 둘째날 일한다면?						
# 일	            1	2	3	4	5	6	7
# t(상담)	        3	5	1	1	2	4	2
# p(돈)         	10	20	10	20	15	40	200
# money(누적 돈)	0	0	0	0	0	20	0
# 	X	O					
							
							
# 	3. 만약 셋째날 일한다면?						
# 일	            1	2	3	4	5	6	7
# t(상담)	        3	5	1	1	2	4	2
# p(돈)         	10	20	10	20	15	40	200
# money(누적 돈)	0	0	10	30	30	45	

# 왜 내 풀이가 메모리 시간 둘다 거의 두배차이인건가;;;;;;ㅠㅠㅠㅠㅠㅠㅠㅠㅠ

# 내풀이    
# 2차원 배열 활용
import sys
n = int(sys.stdin.readline())
dp=[0] * (n+1)
arr = [[0,0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, n+1):
    dp[i] = max(dp[i], dp[i-1]) # dp 최대값 (전날과 현재의 값을 비교함)
    finish = i + arr[i][0] - 1 # p 상담일자가 끝나는 날
    if finish > n: # 만약 n보다 끝나는 날짜가 크다면 퇴사 이후이므로 불가능함
        continue
    dp[finish] = max(dp[i-1] + arr[i][1], dp[finish]) # dp의 값과 finish했을때만의 값을 비교함

print(max(dp)) # 가장 큰 값이 최대값!

# 답지식 풀이
# t와 p를 따로 값을 받아서 진행했음
import sys
n = int(sys.stdin.readline())
dp=[0] * (n+1)
t=[0]
p=[0]
m=0

for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    t.append(a)
    p.append(b)

for i in range(1, n+1):
    dp[i] = max(dp[i], dp[i-1])
    finish = i + t[i] - 1
    if finish > n:
        continue
    dp[finish] = max(dp[finish], dp[i-1] + p[i])

print(max(dp))

