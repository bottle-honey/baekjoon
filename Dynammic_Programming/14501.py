# 퇴사

import sys

input = sys.stdin.readline


n = int(input())
plans = [0]
for _ in range(n):
    a,b= map(int,input().split())

    plans.append((a,b))
dp = [0] * 100

for i in range(1,n+1):
    t,p = plans[i][0],plans[i][1]
    dp[i+t] = max(max(dp[:i+1])+p,dp[i+t])

print(max(dp[:n+2]))
