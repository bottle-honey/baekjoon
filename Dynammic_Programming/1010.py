# 다리 놓기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
dp = [1]+[0]*30
def fac(num:int):
    if dp[num]:
        return dp[num]
    else:
        dp[num] = fac(num-1)*num
        return dp[num]    
    
t = int(input())

for _ in range(t):
    n,m= map(int,input().split())
    print(fac(m)//(fac(n)*fac(m-n)))


