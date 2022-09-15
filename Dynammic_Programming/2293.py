# 동전 1

import sys
input= sys.stdin.readline
coins = []
n,k = map(int,input().split())
for _ in range(n):
    coins.append(int(input()))
dp = [0 for _ in range(k+1)]
dp[0]=1

for coin in coins:
    for j in range(1,k+1):
        if j-coin>=0:
            dp[j] += dp[j-coin]
print(dp[-1])