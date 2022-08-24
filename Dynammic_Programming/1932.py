# 정수 삼각형
import sys
input = sys.stdin.readline

INF = 10000

n = int(input())
tree = []
for _ in range(n):
    tree.append(list(map(int,input().split())))

dp  = [[0]*n for _ in range(n)]
dp[0][0] = tree[0][0]
for i in range(1,n):
    for j in range(i+1): 
        if i-1 >=0:
            dp[i][j] = max(dp[i][j],dp[i-1][j]+tree[i][j])
            if j-1>=0:
                dp[i][j] = max(dp[i][j],dp[i-1][j-1]+tree[i][j])

print(max(dp[n-1]))