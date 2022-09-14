#1,2,3 더하기 3

import sys
from collections import deque
input = sys.stdin.readline
DIV = 1000000009

t = int(input())
cases = []
for _ in range(t):
    n = int(input())
    dp=deque([1])
    for i in range(1,n+1):
        if i==1:
            dp.append(dp[i-1])
        elif i==2:
            dp.append(dp[i-1] + dp[i-2])
        else:
            dp.append(dp[0] + dp[1]+dp[2])
            trash = dp.popleft()
    print(dp[-1]%DIV)