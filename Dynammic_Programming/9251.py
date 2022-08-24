#LCS
import sys
input = sys.stdin.readline
a = list(input().rstrip('\n'))
b = list(input().rstrip('\n'))
dp =[[0]*len(b) for _ in range(len(a))]
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-1] + 1,dp[i][j-1])
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[len(a)-1][len(b)-1])
