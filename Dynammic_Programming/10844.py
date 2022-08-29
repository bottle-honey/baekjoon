#쉬운 계단 수

import sys
input = sys.stdin.readline
DIV = 1000000000
n = int(input())

dp =[[0]*10 for _ in range(n)]
dp[0] = [0] + [1]*9

for i in range(n-1):
    for idx in range(10):
        if idx == 0:
            dp[i+1][1] += dp[i][idx]
        elif idx == 9:
            dp[i+1][8] += dp[i][idx]
        else:
            dp[i+1][idx+1] += dp[i][idx]
            dp[i+1][idx-1] += dp[i][idx]
print(sum(dp[n-1])%DIV)