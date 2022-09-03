import sys
input = sys.stdin.readline

n = int(input())

array = []
for _  in range(n):
    array.append(int(input()))

dp = [0]*n
for i in range(n):
    if i >=3:
        dp[i] = max(dp[i-2]+array[i],dp[i-3]+array[i-1]+array[i],dp[i-1])
    elif i == 0:
        dp[i] = array[i]
    elif i == 1:
        dp[i] = array[i]+array[i-1]
    elif i == 2:
        dp[i] = max(dp[i-2]+array[i],array[i-1]+array[i])
print(dp[n-1])
print(dp)