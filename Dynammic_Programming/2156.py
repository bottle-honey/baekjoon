import sys
input = sys.stdin.readline

n = int(input())

array = [0]
for _  in range(n):
    array.append(int(input()))

dp = [0] 

for i in range(1,n+1):
    if i==1 or i==2:
        dp.append(array[i] + array[i-1])
    else:
        dp.append(max(dp[i-3] + array[i-1]+array[i], dp[i-2]+array[i],dp[i-1]))
print(dp[n])