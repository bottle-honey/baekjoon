# 퇴사

import sys
input = sys.stdin.readline

n= int(input())
arr = [0]

for _ in range(n):
    a,b= map(int,input().split())
    arr.append((a,b))

dp = [0]*(n+2)
for i in range(1,n+1):
    t = arr[i][0]
    p = arr[i][1]
    if i+t<=n:
        dp[i+t] = max(dp[i+t],dp[i]+p)
    dp[i] = max(dp[i],dp[i-1])
print(max(dp))
print(dp)