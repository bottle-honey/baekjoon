#평범한 배낭

import sys

input = sys.stdin.readline
n,k = map(int,input().split())
array = []
for _ in range(n):
    x,y = map(int,input().split())
    array.append((x,y))
dp = [[0]*(k+1) for _ in range(n)]
for i in range(n):
    w,v = array[i]
    for j in range(k+1):
        if i-1>=0:
            if j-w>=0:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v)
            else:
                dp[i][j] = dp[i-1][j]
        else:
            if j-w>=0:
                dp[i][j] = v

print(dp[n-1][k])

