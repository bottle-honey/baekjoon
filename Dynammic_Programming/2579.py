#계단 오르기

import sys
input = sys.stdin.readline

n = int(input())
stairs = []
result = [[0]*2 for _ in range(n)]
for _ in range(n):
    stairs.append(int(input()))
result[0][0],result[0][1] = stairs[0],stairs[0]
for i in range(1,n):
    result[i][1] = result[i-1][0] + stairs[i]
    result[i][0] = max(result[i-2][0],result[i-2][1]) + stairs[i]
print(max(result[n-1]))