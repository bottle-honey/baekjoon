#평범한 배낭

import sys

input = sys.stdin.readline
n,k = map(int,input().split())
array = []
for _ in range(n):
    x,y = map(int,input().split())
    array.append((x,y))
array.sort()
dp = [0]*(k+1)
for w,v in array:
    for idx in range(w,len(dp)):
        dp[idx] = max(dp[idx-w]+v,dp[idx])

print(dp[k])