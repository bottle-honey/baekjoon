#합분해

import sys
input = sys.stdin.readline
DIV = 1000000000
n,k = map(int,input().split())

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(k+1):
        if j == 1:
            dp[i][j] =1
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[n][k]%DIV)