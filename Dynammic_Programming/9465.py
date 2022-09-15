import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    N = int(input())
    val = []
    for _ in range(2):
        val.append(list(map(int,input().split())))
    dp = [[0]*N for _ in range(2)]
    for i in range(2):
        for j in range(2):
            dp[i][j] = val[i][j]
    for j in range(N):
        for i in range(2):
            if j+1<N:
                dp[abs(i-1)][j+1] = max(dp[abs(i-1)][j+1],dp[i][j]+val[abs(i-1)][j+1])
            if j+2<N:
                dp[abs(i-1)][j+2] = max(dp[abs(i-1)][j+2], dp[i][j] + val[abs(i-1)][j+2])
                dp[i][j+2] = max(dp[i][j+2], dp[i][j] + val[i][j+2])
    result = 0
    for i in range(2):
        result = max(result,max(dp[i]))
    print(result)