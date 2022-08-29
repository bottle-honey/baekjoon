#쉬운 계단 수

import sys
input = sys.stdin.readline
DIV = 1000000000
n = int(input())

dp = [(1,2,6)]

for i in range(1,n):
    a = dp[i-1][1]
    b = dp[i-1][0]
    c = dp[i-1][1] + dp[i-1][2]*2
    dp.append((a,b,c))
print(sum(dp[n-1])%DIV)