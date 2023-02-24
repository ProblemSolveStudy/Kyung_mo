import sys
x,y,w,s = map(int,sys.stdin.readline().split())

if 2*w < s:
    print((x+y)*w)
else:
    smaller = min(x,y)
    result = s*smaller
    absxy = abs(x-y)
    if w>s:
        if absxy % 2 == 0:
            result += absxy * s
        else:
            result += (absxy-1) * s + w
    else:
        result += absxy * w
    print(result)