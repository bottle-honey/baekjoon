import sys
input = sys.stdin.readline

n = int(input())

array = []
for _  in range(n):
    array.append(int(input()))

dp = [0] * n

for i in range(n):
    if i==0:
        dp[i] = array[i]
    elif i==1:
        dp[i] = array[i] + dp[i-1]
    elif i==2:
        dp[i] = max(array[i-1],array[i-2]) + array[i]
    else:
        dp[i] = max(dp[i-3] + array[i-1]+array[i], dp[i-2]+array[i],dp[i-1])
print(dp[n-1])